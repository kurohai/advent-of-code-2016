#!/bin/env python

import sys
from pprint import pprint


def get_data(data_file):
    with open(data_file) as f:
        if not p2:
            return parse_lines_p1(f.readlines())
        else:
            return parse_lines_p2(f.readlines())


def parse_lines_p1(lines):
    cols = len(lines[0])
    # print cols
    # print lines
    for line in lines:
        line = line.strip()
        row = [c for c in line.lower()]
        # print 'row:', row
        yield row


def parse_lines_p2(lines):
    return parse_lines_p1(lines)


def decode_message(data):
    cols = len(data[0])
    rows = len(data)
    # print 'c:', cols
    # print 'r:', rows
    chars = dict()
    for i in xrange(cols):
        chars[str(i)] = list()

    for d in data:
        for c in xrange(cols):
            chars[str(c)].append(d[c])
    answer = str()
    for i in xrange(cols):
        answer = answer + most_common(chars[str(i)])
    print
    print(answer)
    print

    answer = str()
    for i in xrange(cols):
        answer = answer + least_common(chars[str(i)])
    print
    print(answer)
    print

def most_common(data):
    return max(set(data), key=data.count)

def least_common(data):
    return min(set(data), key=data.count)



def main(data_file):
    data = [d for d in get_data(data_file)]
    # print(len(data))
    # pprint(data)
    answer = decode_message(data)


if __name__ == '__main__':

    if sys.argv[2] == '1':
        p2 = False
    elif sys.argv[2] == '2':
        p2 = True
    else:
        p2 = False

    infile = sys.argv[1]

    main(infile)
