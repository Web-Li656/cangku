#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from word_count import count_text, filter_invalid_whitespace

print("=== 测试文本字数统计功能 ===")
print()

test_text = "Hello 你好！123, World 世界。"
result = count_text(test_text)
print(f"测试文本: {test_text}")
print(f"总字符数（含）: {result['total_with']}")
print(f"总字符数（不含）: {result['total_without']}")
print(f"汉字: {result['chinese']}")
print(f"字母: {result['letter']}")
print(f"数字: {result['digit']}")
print(f"标点: {result['punct']}")
print(f"空格: {result['space']}")
print()

test_whitespace = "  hello   world  \n\n  test  "
filtered = filter_invalid_whitespace(test_whitespace)
print(f"原始: '{test_whitespace}'")
print(f"过滤后: '{filtered}'")
print()

print("=== 测试完成 ===")
