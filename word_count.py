#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import string


def is_chinese(char):
    return '\u4e00' <= char <= '\u9fff'


def is_punctuation(char):
    if char in string.punctuation:
        return True
    cn_punctuation = '，。！？；：""\'\'（）【】「」『』、…—·《》'
    return char in cn_punctuation


def count_text(text):
    total_with_space = len(text)
    cleaned = ''.join(c for c in text if not is_punctuation(c) and not c.isspace())
    total_without_space = len(cleaned)

    chinese_count = sum(1 for c in text if is_chinese(c))
    letter_count = sum(1 for c in text if c.isalpha() and not is_chinese(c))
    digit_count = sum(1 for c in text if c.isdigit())
    punct_count = sum(1 for c in text if is_punctuation(c))
    space_count = sum(1 for c in text if c.isspace())

    return {
        'total_with': total_with_space,
        'total_without': total_without_space,
        'chinese': chinese_count,
        'letter': letter_count,
        'digit': digit_count,
        'punct': punct_count,
        'space': space_count
    }


def filter_invalid_whitespace(text):
    text = text.replace('\r\n', '\n')
    text = text.replace('\r', '\n')
    while '  ' in text:
        text = text.replace('  ', ' ')
    while '\n\n\n' in text:
        text = text.replace('\n\n\n', '\n\n')
    return text.strip()


def print_welcome():
    print("📊 文本字数统计工具 V1.0")
    print("🔍 核心功能：1. 统计总字符数（含/不含标点/空格）；2. 单独统计汉字、字母、数字、标点、空格数量；3. 支持长文本粘贴，自动过滤无效空白字符")
    print("📋 操作说明：- 输入/粘贴文本后按回车即可统计；- 输入 'clear' 清空当前文本，输入 'exit' 退出程序")
    print("-" * 60)


def print_result(result):
    print("📈 文本字数统计结果：")
    print(f"总字符数（含标点/空格）：{result['total_with']}")
    print(f"总字符数（不含标点/空格）：{result['total_without']}")
    print(f"汉字数量：{result['chinese']}")
    print(f"字母数量：{result['letter']}")
    print(f"数字数量：{result['digit']}")
    print(f"标点符号：{result['punct']}")
    print(f"空格数量：{result['space']}")


def main():
    print_welcome()
    current_text = ""

    while True:
        try:
            user_input = input("📝 请输入/粘贴需要统计的文本（输入'exit'退出）：").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n👋 感谢使用文本字数统计工具！")
            print("💡 如需再次使用，直接运行程序即可～")
            break

        if user_input.lower() == 'exit':
            print("👋 感谢使用文本字数统计工具！")
            print("💡 如需再次使用，直接运行程序即可～")
            break

        if user_input.lower() == 'clear':
            current_text = ""
            print("✅ 已清空当前文本！")
            continue

        if not user_input:
            if not current_text:
                print("⚠️ 提示：未输入任何文本，请重新输入！")
            continue

        filtered = filter_invalid_whitespace(user_input)

        if not filtered:
            print("❌ 错误：输入的文本为空！请输入有效内容后重试。")
            continue

        if len(filtered) > 10000:
            print("⚠️ 警告：文本长度超过10000字符，仅展示前10000字符的统计结果！")
            filtered = filtered[:10000]

        current_text = filtered
        result = count_text(current_text)
        print_result(result)
        print("-" * 60)


if __name__ == "__main__":
    main()
