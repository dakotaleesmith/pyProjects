"""
Example script for use in article showing how to call Python
scripts on the command line.

This script is called with the custom get_color zsh function
by adding the following to your .zshrc file:

function get_color() {
	python3 /Users/dakotaleesmith/pyProjects/zsh_python_tutorial/get_color_value.py "$1"
}
"""

import json
from sys import argv
from insert_data import file_path


def get_data():
    with open(file_path, "r") as f:
        return json.load(f)


def get_color_value(color: str) -> json:
    data = get_data()
    assert color in [
        item.get("color") for item in data
    ], "Color selected not available. Try red!"
    color_dict = {
        item["color"]: item["value"] for item in data if item["color"] == color
    }
    return color_dict


if __name__ == "__main__":
    color = str(argv[1])
    value = get_color_value(color)
    print(value)
