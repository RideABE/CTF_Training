import argparse

def print_previous_lines(input_file, pattern):
    """
    逐行读取日志文件，遇到包含指定 pattern 的行时，直接打印其前一行内容到命令行
    :param input_file: 日志文件路径
    :param pattern: 匹配的字符串
    """
    with open(input_file, 'r', encoding='utf-8') as fin:
        prev_line = None
        for line in fin:
            if pattern in line:
                if prev_line is not None:
                    print(prev_line, end='')  # prev_line 中已包含换行符
            prev_line = line

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="直接在命令行输出日志中出现指定字符串前一条日志记录"
    )
    parser.add_argument("input_file", help="输入的日志文件路径")
    parser.add_argument(
        "--pattern",
        default="'%C2%80'",
        help="匹配的字符串，默认为： '%C2%80'"
    )
    args = parser.parse_args()

    print_previous_lines(args.input_file, args.pattern)
