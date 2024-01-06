#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    args_counter = len(argv) - 1

    args_space = "" if args_counter == 1 else "s"
    args_symbol = "." if args_counter < 1 else ":"

    print("{} argument{}{}".format(args_counter, args_space, args_symbol))
    for i in range(1, args_counter + 1):
        print("{}: {}".format(i, argv[i]))
