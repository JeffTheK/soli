import os
import click
from colorama import Fore, Back, Style

def get_icon(file_name):
    if os.path.isdir(file_name):
        return "🗁"
    elif file_name.endswith(".gitignore"):
        return ""
    elif file_name.endswith(".py"):
        return ""
    elif file_name.endswith(".md"):
        return ""
    elif file_name.endswith(".txt"):
        return ""
    else:
        return "🗋"

@click.command()
@click.option('-v/-h', '--vertical/--horizontal', default=False,)
@click.option('-ni', '--no-icons', is_flag=True, default=False)
def main(vertical, no_icons):
    style = "horizontal"
    if vertical:
        style = "vertical"
    stuff = os.listdir()
    for s in stuff:
        icon = ""
        if not no_icons:
            icon = get_icon(s)

        end = ""
        if style == "horizontal":
            end = " "
        else:
            end = "\n"

        if os.path.isdir(s):
            s = f"{Fore.BLUE}{s}{Fore.RESET}"
        print(f"{icon} {s}", end=end)