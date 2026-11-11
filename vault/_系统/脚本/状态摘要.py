#!/usr/bin/env python3
"""只读查询课程处理状态 JSON，避免每次整份读取。

用法（在 vault 根目录）：
  python3 _系统/脚本/状态摘要.py               打印现场摘要
  python3 _系统/脚本/状态摘要.py --find 文本    按路径、哈希或关键词查完整记录

摘要每次现场生成，不落盘，所以不会过期。
判断某个来源是否已处理时必须用 --find，摘要不能用于去重。
"""
import collections
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FILES = ["课程日程处理状态", "学校网站处理状态", "Teams课程处理状态"]
# 这些键描述“上次到哪、还欠什么”，摘要里展示内容；其余只展示数量。
SHOW = re.compile(r"^(last_|pending|updated_at|schema_version|coverage$)")
MAX_VALUE = 280
MAX_HITS = 5
MAX_HIT = 700


def load(name):
    path = os.path.join(ROOT, "_系统", name + ".json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def clip(value, limit):
    text = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)
    return text if len(text) <= limit else text[:limit] + f"…（共 {len(text)} 字符）"


def status_counts(items):
    counts = collections.Counter()
    for item in items:
        if isinstance(item, dict):
            for key in ("status", "processing_status", "organize_status"):
                if isinstance(item.get(key), str):
                    counts[f"{key}={item[key]}"] += 1
    return dict(counts)


def summary():
    for name in FILES:
        data = load(name)
        print(f"## {name}")
        for key, value in data.items():
            if isinstance(value, list):
                line = f"- {key}: {len(value)} 条"
                counts = status_counts(value)
                if counts:
                    line += f" {clip(counts, MAX_VALUE)}"
                if SHOW.match(key) and value:
                    line += f" 内容: {clip(value, MAX_VALUE)}"
                print(line)
            elif SHOW.match(key):
                print(f"- {key}: {clip(value, MAX_VALUE)}")
            elif isinstance(value, dict):
                print(f"- {key}: {len(value)} 项")
            else:
                print(f"- {key}: {clip(value, 80)}")


def find(needle):
    total = 0
    for name in FILES:
        data = load(name)
        for key, value in data.items():
            items = value if isinstance(value, list) else value.values() if isinstance(value, dict) else [value]
            for item in items:
                text = json.dumps(item, ensure_ascii=False)
                if needle in text:
                    total += 1
                    if total <= MAX_HITS:
                        print(f"[{name}.{key}] {clip(text, MAX_HIT)}")
    print(f"共 {total} 条匹配" + (f"，只显示前 {MAX_HITS} 条，请换更精确的文本" if total > MAX_HITS else ""))


def main(argv):
    if len(argv) == 1:
        summary()
    elif len(argv) == 3 and argv[1] == "--find" and argv[2]:
        find(argv[2])
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv)
