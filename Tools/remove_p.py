import re

pattern = r"</*p/*>|</*br/*>"

def has_p(stringFile: str):
    n = re.findall(pattern, stringFile)
    return len(n)

def remove_p(stringFile: str):
    for _ in range(has_p(stringFile)):
        stringFile = re.sub(pattern, "", stringFile)
    return stringFile