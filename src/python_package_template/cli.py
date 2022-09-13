"""Module that contains the command line application."""

import argparse
from numpy.ctypeslib import load_library
from python_package_template.examples.designs import export_design_json, load_design_json
from typing import List, Optional
from python_package_template.examples.library import *


def get_parser() -> argparse.ArgumentParser:
    """
    Return the CLI argument parser.

    Returns:
        An argparse parser.
    """
    return argparse.ArgumentParser(prog="python-package-template")


def main_script() -> int:
    parser = get_parser()
    opts = parser.parse_args(args=args)
    print(f"script called with arguments: {opts}")
    return 0
