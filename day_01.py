#!/bin/env python

import sys

class Location(dict):
    """dict subclass to allow dotted notation"""

    def __init__(self, *args, **kwargs):
        super(dict, self).__init__(*args, **kwargs)
        self.__dict__ = self
        self.init()

    def init(self):
        """used for subclassing to assign initial attributes"""
        self.compass = int()
        self.steps = {
            '0': int(),
            '1': int(),
            '2': int(),
            '3': int()
        }
        self.total_steps = int()
        self.coords_visited = list()
        self.answer = (0, 0)
        self.x_axis = int()
        self.y_axis = int()

    @property
    def coords(self):
        return (self.x_axis, self.y_axis)

    def _update_coords(self, c, s):
        if c == 0:
            # increase y
            for y in range(int(s)):
                self.y_axis += 1
                self._check_if_visited()
        if c == 1:
            # increase x
            for x in range(int(s)):
                self.x_axis += 1
                self._check_if_visited()
        if c == 2:
            # decrease y
            for y in range(int(s)):
                self.y_axis -= 1
                self._check_if_visited()
        if c == 3:
            # decrease x
            for x in range(int(s)):
                self.x_axis -= 1
                self._check_if_visited()

    def _check_if_visited(self):
        if self.total_steps > 1 and self.coords in self.coords_visited:
            self.answer = self.coords
        else:
            self.coords_visited.append(self.coords)

    def _update_steps(self, c, s):
        self.steps[str(c)] += int(s)
        self.total_steps += int(s)

        if self.answer != (0, 0):
            pass
        else:
            self._update_coords(c, s)
        # print(s, self.total_steps)

    def _normalize_compass(self):
        # if self.compass not in [1, 2, 3, 0]:
        #     print 'Normalizing compass value:', self.compass
        if self.compass == -1:
            self.compass = 3
        elif self.compass == 4:
            self.compass = 0
        elif self.compass not in [1, 2, 3, 0]:
            print 'OOPS:', self.compass


    def _turn_right(self):
        self.compass += 1
        self._normalize_compass()

    def _turn_left(self):
        self.compass -= 1
        self._normalize_compass()

    def _parse_compass(self, compass_nav):
        if compass_nav.lower() == 'r':
            self._turn_right()
        elif compass_nav.lower() == 'l':
            self._turn_left()

    def _parse_distance(self, distance_nav):
        self._update_steps(self.compass, distance_nav)

    def parse_navpoint(self, navpoint):
        self._parse_compass(navpoint[0])
        # print self.steps
        # print navpoint[0], navpoint[1], self.compass, self.steps[str(self.compass)]
        # print self.steps
        self._parse_distance(navpoint[1])
        # print navpoint[0], navpoint[1], self.compass, self.steps[str(self.compass)]
        # print self.steps
        # print
        # print

    def navigate(self, navpoints):
        self.navpoints = navpoints
        for n in self.navpoints:
            self.parse_navpoint(n)
        self._normalize_distance()

    def _normalize_distance(self):
        self.north_south = abs(self.steps['0'] - self.steps['2'])
        self.east_west = abs(self.steps['1'] - self.steps['3'])
        # print self.north_south
        # print self.east_west
        self.distance = self.north_south + self.east_west



def _parse_nav_direction(nav):
    return (nav[0], nav[1:])


def parse_directions(direstions):
    values = direstions.split(', ')
    return [_parse_nav_direction(n) for n in values]


def main(directions):
    navpoints = parse_directions(directions)
    location = Location()
    location.navigate(navpoints)
    # print(location.compass)
    # print(location.steps)
    print('Part 1:\t{0}'.format(location.distance))
    print('Part 2:\t{0}'.format(location.answer[0]+location.answer[1]))
    # a = int()
    # for n in navpoints:
    #     a += int(n[1])



if __name__ == '__main__':
    directions = "R3, L2, L2, R4, L1, R2, R3, R4, L2, R4, L2, L5, L1, R5, R2, R2, L1, R4, R1, L5, L3, R4, R3, R1, L1, L5, L4, L2, R5, L3, L4, R3, R1, L3, R1, L3, R3, L4, R2, R5, L190, R2, L3, R47, R4, L3, R78, L1, R3, R190, R4, L3, R4, R2, R5, R3, R4, R3, L1, L4, R3, L4, R1, L4, L5, R3, L3, L4, R1, R2, L4, L3, R3, R3, L2, L5, R1, L4, L1, R5, L5, R1, R5, L4, R2, L2, R1, L5, L4, R4, R4, R3, R2, R3, L1, R4, R5, L2, L5, L4, L1, R4, L4, R4, L4, R1, R5, L1, R1, L5, R5, R1, R1, L3, L1, R4, L1, L4, L4, L3, R1, R4, R1, R1, R2, L5, L2, R4, L1, R3, L5, L2, R5, L4, R5, L5, R3, R4, L3, L3, L2, R2, L5, L5, R3, R4, R3, R4, R3, R1"
    # directions = "R5, L5, R5, R3"
    # directions = "R2, R2, R2"
    main(directions)
