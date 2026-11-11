#!/usr/bin/env python3
"""提交前扫描：找出不该进公开仓库的内容。

用法：
  python3 scripts/scan_private.py [--terms <私有词表.txt>] [--root .]

私有词表每行一个词（姓名、拼音、学号、学校名、地名等），放在仓库之外。
有命中时退出码为 1。命中不一定是泄露，但每一条都要人看过。
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

MAX_BYTES = 200 * 1024
SELF = "scripts/scan_private.py"

PATTERNS = [
    ("绝对路径", re.compile(r"/Users/[A-Za-z0-9._-]+|/home/[A-Za-z0-9._-]+/|[A-Za-z]:\\Users\\")),
    ("邮箱", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9.-]+")),
    ("手机号", re.compile(r"(?<![0-9])(?:1[3-9][0-9]{9}|01[0-9]-?[0-9]{7,8})(?![0-9])")),
    ("学号样式", re.compile(r"(?<![A-Za-z0-9])[0-9]{2}[A-Z]{3}[0-9]{5}(?![0-9])")),
    ("课程代码样式", re.compile(r"(?<![A-Za-z0-9<])[A-Z]{3,4}[0-9]{4,5}(?![0-9])")),
    ("密钥样式", re.compile(
        r"sk-[A-Za-z0-9_-]{16,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}"
        r"|xox[abp]-[A-Za-z0-9-]{10,}|-----BEGIN [A-Z ]*PRIVATE KEY-----"
        r"|Bearer\s+[A-Za-z0-9._-]{20,}|(?i:set-cookie|cookie)\s*:\s*\S+=\S+"
    )),
]

# 邮箱规则的例外：提交署名里常见的 noreply 地址。
EMAIL_ALLOW = re.compile(r"noreply@|@users\.noreply\.github\.com|@example\.(com|org)")


def list_files(root: Path):
    try:
        out = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-co", "--exclude-standard", "-z"],
            check=True, capture_output=True,
        ).stdout.decode("utf-8")
        files = [root / p for p in out.split("\0") if p]
        if files:
            return files
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    return [p for p in root.rglob("*") if p.is_file() and ".git" not in p.parts]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path("."))
    ap.add_argument("--terms", type=Path, help="私有词表，每行一个词")
    args = ap.parse_args()

    terms = []
    if args.terms:
        terms = [t.strip() for t in args.terms.read_text(encoding="utf-8").splitlines()
                 if t.strip() and not t.startswith("#")]

    hits = 0
    files = list_files(args.root)
    for path in sorted(files):
        rel = path.relative_to(args.root).as_posix()
        size = path.stat().st_size
        if size > MAX_BYTES:
            print(f"[文件过大] {rel}：{size // 1024} KB")
            hits += 1
        for term in terms:
            if term.lower() in rel.lower():
                print(f"[私有词·文件名] {rel}：{term}")
                hits += 1
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"[二进制文件] {rel}")
            hits += 1
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            low = line.lower()
            for term in terms:
                if term.lower() in low:
                    print(f"[私有词] {rel}:{lineno}：{term}")
                    hits += 1
            if rel == SELF:
                continue
            for name, pattern in PATTERNS:
                for m in pattern.finditer(line):
                    if name == "邮箱" and EMAIL_ALLOW.search(m.group(0)):
                        continue
                    print(f"[{name}] {rel}:{lineno}：{m.group(0)[:60]}")
                    hits += 1

    print(f"\n扫描了 {len(files)} 个文件，命中 {hits} 处。")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
