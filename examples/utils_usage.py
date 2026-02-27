# ============================================================================
# 文件: examples/utils_usage.py
# 描述: Utils 使用示例
#
# Bash 快速定位:
#   find . -name "utils_usage.py"
# ============================================================================

"""
Utils 模块使用示例

演示如何使用 FileOps 和 StringOps 进行文件和字符串操作。
"""

from pathlib import Path
from utils.file_ops import FileOps
from utils.string_ops import StringOps


def main():
    """主函数"""
    print("Utils Module Usage Example")
    print("=" * 50)

    # 文件操作
    print("\n1. 文件操作")
    print("   FileOps.write('file.txt', 'Hello, World!')")
    print("   content = FileOps.read('file.txt')")
    print("   返回: 文件内容")

    # 列出目录
    print("\n2. 列出目录")
    print("   items = FileOps.list_dir('path', recursive=True)")
    print("   返回: 目录中的文件/目录列表")

    # 查找文件
    print("\n3. 查找文件")
    print("   files = FileOps.find_files('path', pattern='*.py')")
    print("   返回: 匹配的文件列表")

    # 字符串截断
    print("\n4. 字符串截断")
    print("   truncated = StringOps.truncate('long text...', max_length=10)")
    print("   返回: 截断后的字符串")

    # 字符串转义
    print("\n5. 字符串转义")
    print("   escaped = StringOps.escape('<script>', mode='html')")
    print("   返回: 转义后的字符串")

    # 字符串格式化
    print("\n6. 字符串格式化")
    print("   snake_case = StringOps.format('HelloWorld', style='snake_case')")
    print("   返回: hello_world")
    print("   title_case = StringOps.format('hello world', style='title_case')")
    print("   返回: Hello World")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
