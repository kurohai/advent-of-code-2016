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
fileformat = logging.Formatter('%(asctime)s %(levelname)-9s: %(message)s','%Y-%m-%d %H:%M:%S')
handler.setFormatter(fileformat)


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
        d.components = d.raw.replace('(', ' (')
        d.components = d.components.replace(')', ') ')
        for chars in d.components.split(' '):
            print chars
        yield d


def parse_lines_p2(lines):
    return parse_lines_p1(lines)


def main(data_file):
    data = get_data(data_file)
    log.debug(type(data))
    for d in data:
        # pprint(d)
        pass



if __name__ == '__main__':
    try:
        if sys.argv[2] == '1':
            p2 = False
        elif sys.argv[2] == '2':
            p2 = True
        else:
            p2 = False
        infile = sys.argv[1]
        log.debug('starting main in phase: {0}'.format(sys.argv[2]))
        handler.setLevel(levels[int(sys.argv[3])])
        log.addHandler(handler)
    except:
        log.addHandler(handler)
        log.error('Error in CLI args.')
        print 'usage: ./script.py ./input-file.txt <phase 1 or 2> <logging level 0, 1, 2, or 3>'
        sys.exit(1)
    main(infile)
