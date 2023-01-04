"""
This script loads the sample data used in get_color_value.py.

To get working on local machine, change file_path to local directory.
"""

import json

file_path = "/Users/dakotaleesmith/pyProjects/zsh_python_tutorial/sample_data.json"


def write_sample(json_data: list) -> json:
    with open(file_path, "w") as f:
        json.dump(json_data, f, indent=4)


if __name__ == "__main__":
    data = [
        {"color": "red", "value": "#f00"},
        {"color": "green", "value": "#0f0"},
        {"color": "blue", "value": "#00f"},
        {"color": "cyan", "value": "#0ff"},
        {"color": "magenta", "value": "#f0f"},
        {"color": "yellow", "value": "#ff0"},
        {"color": "black", "value": "#000"},
    ]
    write_sample(data)
