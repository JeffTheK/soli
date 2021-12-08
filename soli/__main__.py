import os

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

def main():
    stuff = os.listdir()
    for s in stuff:
        icon = get_icon(s)
        print(f"{icon} {s}")