import argparse


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root-dir", default=".", help="path to root directory (e.g., ./src)")
    parser.add_argument("--ignore", action="append", default=[], help="regex pattern to ignore file paths")
    parser.add_argument("files", nargs="+", help="files to be processed")
    return parser.parse_args()
