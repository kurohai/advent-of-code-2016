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
        return parse_lines(f.readlines())


def parse_lines(lines):
    names = list()
    for line in lines:
        names.append(parse_line(line))
    return names


def parse_line(line):
    d = dicto()
    d.cipher = re.search('[0-9]+', line).group()
    d.codename = line.replace(d.cipher, '')[:-1]
    return d


def decode_name(sector, codename):
    sector_mod = int(sector) % 26
    name = str()
    for char in codename:
        name = name + do_math(sector_mod, char)

    return name, sector


def do_math(cipher, char):
    if char == '-':
        return ' '
    else:
        ordval = ord(char)
        newval = ordval + int(cipher)
        if newval > 122:
            newval -= 26
        return chr(newval)


def main(data_file):
    data = get_data(data_file)
    for name in data:
        print decode_name(name.cipher, name.codename)


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
