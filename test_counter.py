#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""测试文本统计功能"""

import sys
sys.path.insert(0, r'd:\trae-code\cangku - 1')
from text_counter import analyze_text

# 测试用例
test_cases = [
    "Hello World",
    "你好世界",
    "Hello 世界 123！",
    "Python3.9 发布了！",
    "  前后有空格  ",
]

print("=" * 60)
print("文本字数统计工具 - 功能测试")
print("=" * 60)

for i, text in enumerate(test_cases, 1):
    print(f"\n测试 {i}: '{text}'")
    print("-" * 40)
    stats = analyze_text(text)
    print(f"  总字符数（含标点/空格）：{stats['total_with_punctuation']}")
    print(f"  总字符数（不含标点/空格）：{stats['total_without_punctuation']}")
    print(f"  汉字数量：{stats['chinese_chars']}")
    print(f"  字母数量：{stats['letters']}")
    print(f"  数字数量：{stats['digits']}")
    print(f"  标点符号：{stats['punctuation']}")
    print(f"  空格数量：{stats['spaces']}")

print("\n" + "=" * 60)
print("测试完成！")
print("=" * 60)
