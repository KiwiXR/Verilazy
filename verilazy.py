import argparse
import re


def verilazy(args):
    fmt_list = []
    if args.format != "":
        fmt_list.append(args.format)
        args.batch -= 1
    for _ in range(args.batch):
        fmt_list.append(input())
    print("INFO: {} formats read.".format(len(fmt_list)))
    full_list = []
    for cnt in range(args.counter):
        res_list = []
        for fmt in fmt_list:
            fmt = re.sub(r'<c>', str(cnt), fmt)
            n = len(re.findall(r'<[ns]>', fmt))
            retry = 0
            retry_lim = 10
            while retry <= retry_lim:
                print(">> " + fmt)
                if retry != 0:
                    print("INFO: {} params to be filled [Retry {}/{}]".format(n, retry, retry_lim))
                params = input().strip().split()
                if len(params) != n:
                    print("ERROR: Wrong number of params!")
                    retry += 1
                    continue
                flag = True
                tmp_fmt = fmt
                for i in range(n):
                    r_type = re.search(r'<[ns]>', tmp_fmt).group()
                    if r_type[1] == 'n' and not params[i].isdigit():
                        print("ERROR: Wrong type of param {}: {} [Integer Expected]".format(i, params[i]))
                        retry += 1
                        flag = False
                        break
                    tmp_fmt = re.sub(r_type, params[i], tmp_fmt, count=1)
                if not flag:
                    continue
                res_list.append(tmp_fmt)
                break

            if retry == retry_lim + 1:
                raise PermissionError("Don't play with me!")
        f = None
        if args.output != "":
            f = open(args.output, 'w')
        full_list += res_list
        for res in res_list:
            msg = "<< " + res
            print(msg)
            if f is not None:
                f.write(msg)
        print("INFO: Round {} OK.\n".format(cnt + 1))
        if f is not None:
            f.close()
    print("INFO: All work done!")
    print("SUM UP:\n")
    for item in full_list:
        print(item)
    print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Verilazy: Verilog Lazy Code Generator",
                                     usage="python verilazy.py [-b int] [-f str] [-s str] [-c int] [-o str]\n"
                                           "[str lines]",
                                     epilog="format: {<n> : number, <s> : string, <c> : auto counter}\n"
                                            "Note that numbers are same as strings except for extra type check")
    parser.add_argument("-b", "--batch", default=1, metavar="BATCH",
                        help="batch size of formats", type=int)
    parser.add_argument("-f", "--format", default="", metavar="FORMAT",
                        help="format of single line", type=str)
    parser.add_argument("-s", "--signal", default="<>", metavar="SIGNAL",
                        help="pair of signal for replacement", type=str)
    parser.add_argument("-c", "--counter", default=1, metavar="COUNTER",
                        help="maximum value of auto counter", type=int)
    parser.add_argument("-o", "--output", default="", metavar="OUTFILE",
                        help="output file", type=str)
    args = parser.parse_args()
    print(args)
    if len(args.signal) != 2:
        raise ValueError("signal pair length should be 2!")
    if args.batch <= 0:
        raise ValueError("batch size of formats should be greater than 0!")
    verilazy(args)
