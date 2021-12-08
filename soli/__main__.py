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
@click.option('-nc', '--no-color', is_flag=True, default=False)
def main(vertical, no_icons, no_color):
    style = "horizontal"
    if vertical:
        style = "vertical"

    stuff = os.listdir()
    stuff.sort(key=lambda s: os.path.isdir(s))
    for s in stuff:
        icon = ""
        if not no_icons:
            icon = get_icon(s)

        end = ""
        if style == "horizontal":
            end = " "
        else:
            end = "\n"

        size = ""
        if vertical:
            if os.path.isfile(s):
                size = Fore.GREEN + str(os.stat(s).st_size).ljust(4) + " " + Fore.RESET
            else:
                size = Fore.LIGHTBLACK_EX + "- ".rjust(4) + Fore.RESET

        if os.path.isdir(s) and not no_color:
            s = f"{Fore.BLUE}{s}{Fore.RESET}"
        print(f"{size}{icon} {s}", end=end)