import re

pattern = r"<details><summary>"
replace = "<details>\n<summary>"

def has_details(stringFile: str):
    n = re.findall(pattern, stringFile)
    return len(n)

def fix_details(stringFile: str):
    for _ in range(has_details(stringFile)):
        stringFile = re.sub(pattern, replace, stringFile)
    return stringFile