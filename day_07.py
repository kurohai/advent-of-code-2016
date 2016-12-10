#!/bin/env python


import re
import sys
import operator
import logging
from pprint import pprint

from dicto import dicto


hyper_regex = re.compile('\[[a-z]+\]')
not_hyper_regex = re.compile('(\][a-z]+\[|[a-z]+\[|\][a-z]+)')

levels = [logging.ERROR, logging.WARN, logging.INFO, logging.DEBUG]
log = logging.Logger(__name__)
handler = logging.StreamHandler()
handler.setLevel(levels[int(sys.argv[3])])
fileformat = logging.Formatter('%(asctime)s %(levelname)-9s: %(message)s','%Y-%m-%d %H:%M:%S')
handler.setFormatter(fileformat)
log.addHandler(handler)


def get_data(data_file):
    with open(data_file) as f:
        return parse_lines(f.readlines())


def parse_lines(lines):
    data = list()
    for line in lines:
        data.append(parse_line(line))
    return data


def parse_line(line):
    d = dicto()
    line = line.strip()
    d.raw = line
    d.blocks = list()
    d.ssl_aba = list()
    d.hypernet_blocks = list()
    d.ssl_bab = list()

    i = 0
    lina = line.replace('[', ',')
    lina = lina.replace(']', ',')
    for L in lina.split(','):
        i += 1
        if i % 2 != 0:
            d.blocks.append(L)
            tmp = do_get_ssl(L)
            if tmp:
                for x in tmp:
                    d.ssl_aba.append(x)
        else:
            d.hypernet_blocks.append(L)
            tmp = do_get_ssl(L)
            if tmp:
                for x in tmp:
                    d.ssl_bab.append(x)
    # pprint(d)
    return d


def do_check_abba(line):
    for i, c in enumerate(line[:-3]):
        c1 = line[i]
        c2 = line[i+1]
        c3 = line[i+2]
        c4 = line[i+3]
        # print line
        # print ' '*i + c1 + c2 + c3 + c4

        if c1 != c2 and c3 != c4:
            if c1 == c4 and c2 == c3:
                # print line
                # print line[:-3]
                # print ' '*i + c1 + c2 + c3 + c4
                return True
    return False


def do_get_ssl(line):
    ssl_aba_bab = list()
    for i, c in enumerate(line[:-2]):
        c1 = line[i]
        c2 = line[i+1]
        c3 = line[i+2]
        print line
        print ' '*i + c1 + c2 + c3

        if c1 != c2 and c1 == c3:
            ssl_aba_bab.append(c1+c2+c3)
            print ' '*i + c1 + c2 + c3, '<--------------'
    if ssl_aba_bab:
        return ssl_aba_bab


def check_for_abba(addr):
    for block in addr.hypernet_blocks:
        if do_check_abba(block):
            return False
    for block in addr.blocks:
        if do_check_abba(block):
            return True


def check_for_ssl(addr):
    for aba in addr.ssl_aba:
        if addr.ssl_bab:
            if do_check_ssl(aba, addr.ssl_bab):
                return True


def do_check_ssl(aba, babs):
    target_bab = aba[1] + aba[0] + aba[1]
    print 'target aba:', aba
    print 'target bab:', target_bab
    print 'checking:', babs
    if target_bab in babs:
        print 'found!'
        return True

def main(data_file):
    data = get_data(data_file)
    answer_abba = int()
    answer_ssl = int()
    for d in data:
        if check_for_abba(d):
            answer_abba += 1
        if check_for_ssl(d):
            answer_ssl += 1
        # break
    print answer_abba
    print answer_ssl



if __name__ == '__main__':
    args = sys.argv[1:]
    if sys.argv[2] == '1':
        p2 = False
    elif sys.argv[2] == '2':
        p2 = True
    else:
        p2 = False
    infile = sys.argv[1]
    log.debug('starting main in phase: {0}'.format(sys.argv[2]))
    main(infile)
