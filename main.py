"""Copy as Path Many — Copy many file paths to the clipboard from a list or a folder glob."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='copy_as_path_many',
        description='Copy many file paths to the clipboard from a list or a folder glob.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Copy as Path Many')
    print('A clipboard full of quoted paths.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
