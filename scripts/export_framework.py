#!/usr/bin/env python3
"""把清单里的文件从私人库复制到 vault/，并套用替换表。

用法：
  python3 scripts/export_framework.py --vault <私人库> --manifest <清单.txt> \
      --replacements <替换表.json> --out vault [--dry-run]

清单每行一个相对路径；以 / 结尾的行表示整个目录；以 ! 开头的行表示排除该文件。
替换表是 JSON：{"literal": [[原文, 替换], ...], "regex": [[正则, 替换], ...]}。
替换表里有真实姓名，请放在仓库之外，不要提交。
只处理清单里的文件；仓库里手写的空白页不会被覆盖，除非它也在清单里。
"""
import argparse
import json
import re
import shutil
from pathlib import Path

TEXT_SUFFIXES = {".md", ".py", ".json", ".yaml", ".yml", ".txt", ".toml", ".css", ".sh"}


def iter_sources(vault: Path, manifest: Path):
    lines = [l.strip() for l in manifest.read_text(encoding="utf-8").splitlines()]
    excluded = {vault / l[1:].strip() for l in lines if l.startswith("!")}
    for path in _iter_included(vault, lines):
        if path not in excluded:
            yield path


def _iter_included(vault: Path, lines):
    for line in lines:
        if not line or line.startswith("#") or line.startswith("!"):
            continue
        src = vault / line.rstrip("/")
        if line.endswith("/"):
            for path in sorted(src.rglob("*")):
                if path.is_file() and path.name != ".DS_Store":
                    yield path
        elif src.is_file():
            yield src
        else:
            print(f"缺失：{line}")


def apply(text: str, table: dict) -> str:
    # 先套正则再套字面替换，免得占位符里的字母影响正则的边界判断。
    for pattern, new in table.get("regex", []):
        text = re.sub(pattern, new, text)
    for old, new in table.get("literal", []):
        text = text.replace(old, new)
    return text


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", required=True, type=Path)
    ap.add_argument("--manifest", required=True, type=Path)
    ap.add_argument("--replacements", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    table = json.loads(args.replacements.read_text(encoding="utf-8"))
    for src in iter_sources(args.vault, args.manifest):
        rel = src.relative_to(args.vault)
        dst = args.out / rel
        if args.dry_run:
            print(f"将导出：{rel}")
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.suffix.lower() in TEXT_SUFFIXES:
            dst.write_text(apply(src.read_text(encoding="utf-8"), table), encoding="utf-8")
        else:
            shutil.copy2(src, dst)
        print(f"已导出：{rel}")


if __name__ == "__main__":
    main()
