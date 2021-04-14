#!/usr/bin/env python3

import sys
import argparse

parser = argparse.ArgumentParser(description="This is Tim Ostrander's script")

parser.add_argument('-m BASIC', dest='', help='Enter some text')
parser.add_argument('-i', '--integer', dest='varInteger', metavar='[an integer]', default=10, type=int, required=False, help='<required> Enter a simple Integer')
parser.add_argument('-d', '--float', dest='varFloat', metavar='[a float]', default=10.0, type=float, required=False, help='Enter a simple Float')
parser.add_argument('-s', '--string', dest='varString', metavar='[a string]', default='hello', type=str, required=False, help='Enter a simple String')
parser.add_argument('-l', dest='varList', metavar='[strings]', default=[], nargs='+', required=False, help='Enter a list of strings (space delimited)')
parser.add_argument('-t', '--set-true', dest='bool_t', default=False, action='store_true', required=False, help='Toggle from default False to true')
parser.add_argument('-f', '--set-false', dest='bool_f', default=True, action='store_false', required=False, help='Toggle from default True to False')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')

if len(sys.argv) == 1:
	print(parser.print_help())
	exit(0)
