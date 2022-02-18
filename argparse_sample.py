# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 15:09:12 2022

@author: InnoP
"""

import argparse

def main():
    parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='no input',
                        help='test input')
    opt = parser.parse_args()
    print('Input:', opt.input)

if __name__ == "__main__":
    main()