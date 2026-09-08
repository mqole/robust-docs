import common
import re

pattern = r"</*hr/*>"

def has_hr(stringFile: str):
    n = re.findall(pattern, stringFile)
    return len(n)

def convert_hr(stringFile: str):
    for _ in range(has_hr(stringFile)):
        stringFile = re.sub(pattern, "<hr/>", stringFile)
    return stringFile