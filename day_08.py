#!/bin/env python

import sys
from dicto import dicto
from pprint import pprint


import geometry







def main():
    Rect = geometry.Rect
    rect1=Rect( 0,  0, 10, 10)
    rect2=Rect(80, 50, 10, 10)
    print(rect1.distance_to_rect(rect2))






if __name__ == '__main__':
    main()
