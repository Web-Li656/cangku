#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from word_count import count_text, filter_invalid_whitespace

print("=== 测试文本字数统计功能 ===\n")

test_cases = [
    ("Hello 你好！123, World 世界。", "中英混合"),
    ("   多余   空格   ", "空白字符过滤"),
    ("", "空文本"),
    ("12345", "纯数字"),
    ("测试汉字", "纯汉字"),
]

for text, desc in test_cases:
    print(f"【{desc}】输入: '{text}'")
    if text:
        result = count_text(text)
        print(f"  总字符(含): {result['total_with']}")
        print(f"  总字符(不含): {result['total_without']}")
        print(f"  汉字: {result['chinese']}, 字母: {result['letter']}, 数字: {result['digit']}")
        print(f"  标点: {result['punct']}, 空格: {result['space']}")
    print()

print("=== 测试完成 ===")
