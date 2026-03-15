#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文本字数统计工具 V1.0
功能：统计文本中的字符数、汉字、字母、数字、标点和空格
"""

import re
import sys


def print_welcome():
    """打印欢迎语"""
    print("\n" + "=" * 50)
    print("📊 文本字数统计工具 V1.0")
    print("=" * 50)
    print("\n🔍 核心功能：")
    print("   1. 统计总字符数（含/不含标点/空格）")
    print("   2. 单独统计汉字、字母、数字、标点、空格数量")
    print("   3. 支持长文本粘贴，自动过滤无效空白字符")
    print("\n📋 操作说明：")
    print("   - 输入/粘贴文本后按回车即可统计")
    print("   - 输入 'clear' 清空当前文本")
    print("   - 输入 'exit' 退出程序")
    print("=" * 50 + "\n")


def print_result(stats):
    """打印统计结果"""
    print("\n" + "-" * 50)
    print("📈 文本字数统计结果：")
    print("-" * 50)
    print(f"总字符数（含标点/空格）：{stats['total_with_punctuation']}")
    print(f"总字符数（不含标点/空格）：{stats['total_without_punctuation']}")
    print(f"汉字数量：{stats['chinese_chars']}")
    print(f"字母数量：{stats['letters']}")
    print(f"数字数量：{stats['digits']}")
    print(f"标点符号：{stats['punctuation']}")
    print(f"空格数量：{stats['spaces']}")
    print("-" * 50 + "\n")


def is_chinese_char(char):
    """判断字符是否为汉字（包括CJK统一表意文字）"""
    code = ord(char)
    # CJK统一表意文字基本区
    if 0x4E00 <= code <= 0x9FFF:
        return True
    # CJK统一表意文字扩展A区
    if 0x3400 <= code <= 0x4DBF:
        return True
    # CJK统一表意文字扩展B区
    if 0x20000 <= code <= 0x2A6DF:
        return True
    # CJK兼容字符
    if 0xF900 <= code <= 0xFAFF:
        return True
    return False


def analyze_text(text):
    """分析文本统计信息"""
    stats = {
        'total_with_punctuation': 0,
        'total_without_punctuation': 0,
        'chinese_chars': 0,
        'letters': 0,
        'digits': 0,
        'punctuation': 0,
        'spaces': 0
    }

    # 清理文本：去除首尾空白，但保留中间的空格
    text = text.strip()

    if not text:
        return stats

    # 总字符数（含标点/空格）
    stats['total_with_punctuation'] = len(text)

    # 遍历每个字符进行分类统计
    for char in text:
        # 汉字
        if is_chinese_char(char):
            stats['chinese_chars'] += 1
            stats['total_without_punctuation'] += 1
        # 字母（不包括汉字）
        elif char.isalpha():
            stats['letters'] += 1
            stats['total_without_punctuation'] += 1
        # 数字
        elif char.isdigit():
            stats['digits'] += 1
            stats['total_without_punctuation'] += 1
        # 空格
        elif char.isspace():
            stats['spaces'] += 1
        # 标点符号（其他字符）
        else:
            stats['punctuation'] += 1

    return stats


def is_punctuation(char):
    """判断字符是否为标点符号"""
    # 中文标点
    chinese_punctuation = '，。、；：？！""''（）【】《》…—～·'
    # 英文标点
    english_punctuation = ',.;:!?"\'()[]{}<>/-_=+@#$%^&*|\\'

    return char in chinese_punctuation or char in english_punctuation


def main():
    """主程序"""
    print_welcome()

    while True:
        try:
            # 文本输入引导
            user_input = input("📝 请输入/粘贴需要统计的文本（输入'exit'退出）：\n")

            # 处理特殊命令
            if user_input.lower() == 'exit':
                print("\n👋 感谢使用文本字数统计工具！")
                print("💡 如需再次使用，直接运行程序即可\n")
                break

            elif user_input.lower() == 'clear':
                print("\n✅ 已清空当前文本！\n")
                continue

            # 检查空输入
            if not user_input.strip():
                print("\n⚠️ 提示：未输入任何文本，请重新输入！\n")
                continue

            # 处理多行输入（检测是否有未完成的输入）
            text = user_input

            # 长文本警告
            if len(text) > 10000:
                print("\n⚠️ 警告：文本长度超过10000字符，仅展示前10000字符的统计结果！")
                text = text[:10000]

            # 统计文本
            try:
                stats = analyze_text(text)

                # 检查结果是否为空
                if stats['total_with_punctuation'] == 0:
                    print("\n❌ 错误：输入的文本为空！请输入有效内容后重试。\n")
                    continue

                # 打印统计结果
                print_result(stats)

            except Exception as e:
                print(f"\n❌ 错误：输入格式异常，请检查文本后重新粘贴！")
                print(f"   详细信息：{str(e)}\n")
                continue

        except KeyboardInterrupt:
            print("\n\n👋 感谢使用文本字数统计工具！")
            print("💡 如需再次使用，直接运行程序即可\n")
            break
        except EOFError:
            print("\n\n👋 感谢使用文本字数统计工具！")
            print("💡 如需再次使用，直接运行程序即可\n")
            break


if __name__ == "__main__":
    main()
