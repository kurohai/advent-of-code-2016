#!/bin/env python


import sys


top_bounds = [1, 2, 3]
right_bounds = [3, 6, 9]
bottom_bounds = [7, 8, 9]
left_bounds = [1, 4, 7]

coords = {
    '1':  (3, 5),
    '2':  (2, 4),
    '3':  (3, 4),
    '4':  (4, 4),
    '5':  (1, 3),
    '6':  (2, 3),
    '7':  (3, 3),
    '8':  (4, 3),
    '9':  (5, 3),
    '10': (2, 2),
    '11': (3, 2),
    '12': (4, 2),
    '13': (3, 1),
}

coord_list = [v for k, v in coords.items()]


def U(n):
    # + y
    if p2:
        oc = coords[str(n)]
        nc = (oc[0], oc[1]+1)
        # print 'New coords:', nc
        if nc in coord_list:
            for k, v in coords.items():
                if v == nc:
                    return k
        else:
            return n
    else:
        if n not in top_bounds:
            return n - 3
        else:
            return n


def D(n):
    # - y
    if p2:
        oc = coords[str(n)]
        nc = (oc[0], oc[1]-1)
        # print 'New coords:', nc
        if nc in coord_list:
            for k, v in coords.items():
                if v == nc:
                    return k
        else:
            return n
    else:

        if n not in bottom_bounds:
            return n + 3
        else:
            return n


def R(n):
    # + x
    if p2:
        oc = coords[str(n)]
        nc = (oc[0]+1, oc[1])
        # print 'New coords:', nc
        if nc in coord_list:
            for k, v in coords.items():
                if v == nc:
                    return k
        else:
            return n

    else:
        if n not in right_bounds:
            return n + 1
        else:
            return n


def L(n):
    # - x
    if p2:
        oc = coords[str(n)]
        nc = (oc[0]-1, oc[1])
        # print 'New coords:', nc
        if nc in coord_list:
            for k, v in coords.items():
                if v == nc:
                    return k
        else:
            return n
    else:

        if n not in left_bounds:
            return n - 1
        else:
            return n


def parse_lines(lines):
    codes = list()
    for line in lines:
        codes.append([x.upper() for x in line.strip()])
    return codes


def get_super_secret_code_from_file(secret_squirrel_file):
    with open(secret_squirrel_file) as f:
        return parse_lines(f.readlines())


def decode_code(pin, code):
    for c in code:
        # print c, pin
        pin = eval(c)(pin)
        # print c, pin
    return pin


def main(code_file):
    codes = get_super_secret_code_from_file(code_file)
    pin = 5
    for code in codes:
        pin = decode_code(pin, code)
        if pin == str(10):
            print 'A'
        elif pin == str(11):
            print 'B'
        elif pin == str(12):
            print 'C'
        elif pin == str(13):
            print 'D'
        else:
            print pin


if __name__ == '__main__':
    p2 = sys.argv[2]
    if p2 == str(1):
        p2 = False
    elif p2 == str(2):
        p2 = True
    else:
        print 'now ya done fucked up'
        sys.exit(0)
    main(sys.argv[1])
