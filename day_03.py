#!/bin/env python

import sys





def parse_lines_v2(lines):
    c1 = [i[0] for i in lines]
    c2 = [i[1] for i in lines]
    c3 = [i[2] for i in lines]

    i = len(lines)
    c = 0
    t1 = list()
    t2 = list()
    t3 = list()
    all_those_triangles = list()

    while c < i:
        l = lines[c].strip().split()
        # print l
        t1.append(int(l[0]))
        t2.append(int(l[1]))
        t3.append(int(l[2]))
        c += 1
        if c % 3 == 0:
            t1.sort()
            all_those_triangles.append(t1)
            t1 = list()

            t2.sort()
            all_those_triangles.append(t2)
            t2 = list()

            t3.sort()
            all_those_triangles.append(t3)
            t3 = list()
        # print c

    return all_those_triangles



def parse_lines(lines):
    for line in lines:
        yield [int(i) for i in line.strip().split()]


def get_data(data_file):
    with open(data_file) as f:
        if p2:
            return parse_lines_v2(f.readlines())
        else:
            return parse_lines(f.readlines())


def main(data_file):
    data = [d for d in get_data(data_file)]
    i = int()
    for d in data:
        d.sort()
        if d[0] + d[1] > d[2]:
            i += 1
    print i




if __name__ == '__main__':
    if sys.argv[2] == '1':
        p2 = False
    elif sys.argv[2] == '2':
        p2 = True
    main(sys.argv[1])
