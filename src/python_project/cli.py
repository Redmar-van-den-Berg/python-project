"""
Module that contains the command line app, so we can still import __main__
without executing side effects
"""

import argparse

parser = argparse.ArgumentParser(description="Description of command.")
parser.add_argument("name", default="world", required=False)


def main(args):
    args = parser.parse_args(args)
    print(f"Hello, {args.name}")
