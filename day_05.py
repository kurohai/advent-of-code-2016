#!/bin/env python

import md5

def main(door_id):
    password = str()
    password_pos = dict()
    for i in xrange(8):
        password_pos[str(i)] = False
    print password_pos

    while len(password) < 8:
        for i in range(999*999, 9999*9999):
            code = md5.new('{doorid}{index}'.format(doorid=door_id, index=i)).hexdigest()
            if code.startswith('00000') and code[5] in ['0', '1', '2', '3', '4', '5', '6', '7']:
                if password_pos[code[5]] is False:
                    password_pos[code[5]] = code[6]
                    print code, i
                    password = password + code[5]
            if len(password) == 8:
                break
    p = str()
    print password_pos
    for i in xrange(8):
        print password_pos[str(i)]
        p = p+password_pos[str(i)]
    print p



if __name__ == '__main__':
    # door_id = 'abc'
    door_id = 'uqwqemis'
    main(door_id)


# 1a31a31a
# 4D44t6De3DZC
# 4D44t6De3DZC

# 05ace8e3
