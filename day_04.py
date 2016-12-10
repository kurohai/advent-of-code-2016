#!/bin/env python


import re
import sys
import operator
import logging
from pprint import pprint

from dicto import dicto


levels = [logging.ERROR, logging.WARN, logging.INFO, logging.DEBUG]
log = logging.Logger(__name__)
handler = logging.StreamHandler()
handler.setLevel(levels[int(sys.argv[3])])
fileformat = logging.Formatter('%(asctime)s %(levelname)-9s: %(message)s','%Y-%m-%d %H:%M:%S')
handler.setFormatter(fileformat)
log.addHandler(handler)


def get_data(data_file):
    with open(data_file) as f:
        if not p2:
            return parse_lines_p1(f.readlines())
        else:
            return parse_lines_p2(f.readlines())


def parse_lines_p1(lines):
    # results = list()
    for line in lines:
        line = line.strip()
        d = dicto()
        d.raw = line
        d.ccount = dicto()
        d.checksum = re.search('\[[a-z]+\]', line).group().replace('[', '').replace(']', '')
        d.id = re.search('[0-9]+', line).group()
        d.chars = re.search('[a-z-]+', line).group().replace('-', '')
        log.debug('parsed data: {0}  {1}  {2}'.format(d.checksum, d.id, d.chars))
        yield d


def parse_lines_p2(lines):
    return parse_lines_p1(lines)


def count_chars(data):
    log.debug(type(data))
    results = list()
    for d in data:
        log.debug('pre-count:  {0}'.format(d))
        chars = d.chars
        d.ccount_list = dicto()
        for i in xrange(10):
            d.ccount_list[i] = list()
        for c in set(chars):

            # print c, d.chars.count(c)
            # d.ccount[c] = d.chars.count(c)
            d.ccount_list[d.chars.count(c)].append(c)
        d.ccount_list = {a: b for a, b in d.ccount_list.items() if b != []}

        results.append(d)
        log.debug('post-count: {0}'.format(d))
    return results


def find_real(data):
    answer = int()
    i = 0
    for d in data:
        i += 1
        print i
        pprint(d)
        d.ccount_v = sorted(d.ccount.items(), key=operator.itemgetter(1))
        d.ccount_k = sorted(d.ccount.items(), key=operator.itemgetter(0))
        tmp = str()
        for k, v in d.ccount_list.items():
            v.sort()
            d.ccount_list[k] = v
        for k, v in reversed(d.ccount_list.items()):
            print k, v
            for n in v:
                if len(tmp) < 5:
                    tmp = tmp + n

        if tmp == d.checksum:
            print 'correct!'
            # log.info('{}\t{}'.format(tmp, d.checksum))
            answer += int(d.id)
            with open('./day_04_01_answers.txt', 'ab') as f:
                f.write(d.raw.replace(re.search('\[[a-z]+\]', d.raw).group(), '') + '\n')
        log.info('{}\t{}'.format(tmp, d.checksum))
        print

    return answer
# < 1146868
# < 240877
# > 121500
# 158835

def main(data_file):
    data = get_data(data_file)
    log.debug(type(data))
    results = count_chars(data)
    answer = find_real(results)
    print answer


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
