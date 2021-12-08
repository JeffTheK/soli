import os
import click

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
def main(vertical):
    style = "horizontal"
    if vertical:
        style = "vertical"
    stuff = os.listdir()
    for s in stuff:
        icon = get_icon(s)
        end = ""
        if style == "horizontal":
            end = " "
        else:
            end = "\n"
        print(f"{icon} {s}", end=end)