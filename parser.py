import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Async file sorter")
    parser.add_argument("source", help="Source folder")
    parser.add_argument("output", help="Output folder")
    return parser.parse_args()
