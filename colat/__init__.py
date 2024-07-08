
__version__ = "0.2.0"

import argparse

import keyboard
import pyautogui
import pyperclip
from actus import info


class ParserArguments(argparse.Namespace):
    uppercase_mode: bool


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="colat",
        description="Copy color under cursor to clipboard",
        add_help=False
    )
    parser.add_argument(
        "-h", "--help",
        action="help",
        help="Show this help message and exit",
        default=argparse.SUPPRESS
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"%(prog)s: v{__version__}",
        help="Show `%(prog)s` version number and exit"
    )
    parser.add_argument(
        "-u", "--uppercase",
        action="store_true",
        dest="uppercase_mode",
        help="Use uppercase representation for hex letter"
    )

    args = ParserArguments()
    parser.parse_args(namespace=args)

    info("Waiting for $[CTRL] event...")
    keyboard.wait("ctrl")
    point = pyautogui.position()
    info(f"Point: $[{point.x, point.y}]")
    r, g, b = pyautogui.pixel(*map(int, point))
    hex_code = (
        f"#{r:02X}{g:02X}{b:02X}"
        if args.uppercase_mode
        else f"#{r:02x}{g:02x}{b:02x}"
    )
    pyperclip.copy(hex_code)
    info(f"Copied hex code `$[{hex_code}]` to clipboard")

    return 0
