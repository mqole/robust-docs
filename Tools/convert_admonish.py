import common
import re

# Dict of mdbook admonish types : corresponding Docusaurus syntax we want to use.
# If an admonish already has a custom title, we'll use the 2nd item in the array as a fallback
admonishDict = {
    "note" : "note",
    "abstract" : ["note[Abstract]", "note"],
    "info" : "info",
    "tip" : "tip",
    "success" : ["tip[Success]", "tip"],
    "question" : ["info[Question]", "info"],
    "warning" : "warning",
    "failure" : ["danger[Failure]", "danger"],
    "danger" : "danger",
    "bug" : ["warning[Bug]", "warning"],
    "example" : ["info[Example]", "info"],
    "quote" : ["note[Quote]", "note"]
}

startPattern = "(`*)admonish"
midPattern = "(\n|.)*?"

def has_admonish(stringFile: str):
    n = re.findall(startPattern, stringFile)
    return len(n)

def convert_admonish_blocks(stringFile: str):
    for _ in range(has_admonish(stringFile)):
        stringFile = convert_next_admonish_block(stringFile)
    try:
        if has_admonish > 0:
            print("\n" + has_admonish + " blocks still in file, something's gone wrong.")
    finally:
        return stringFile

def convert_next_admonish_block(stringFile: str):
    # Count the number of ` characters.
    admonishStart = re.search(startPattern, stringFile)
    countBacktick = admonishStart.group(1).count("`")
    backtickPattern = "`{"+str(countBacktick)+"}"

    # Look for the next instance of that many ` characters occurring - thats the end of our admonish block.
    admonishPattern2 = startPattern + midPattern + backtickPattern
    admonishBlock = re.search(admonishPattern2, stringFile).group()

    firstLine = admonishBlock.splitlines()[0]

    # We check for a title first.
    try:
        title = re.search("\"(.*)\"", firstLine).group(1)
        hasTitle = True
    except:
        hasTitle = False

    # Then substitute our new type.
    type = re.search(startPattern+" (.*?)( |\Z)", firstLine).group(2)
    newType = admonishDict.get(type)
    # If we don't have a title, we can use the old mdbook type as a new title.
    if isinstance(newType, list):
        newType:str = newType[0] if not hasTitle else newType[1]
    
    # Feed new type and title back into our first line.
    newFirstLine = "`" * countBacktick + newType
    if hasTitle:
        newFirstLine = newFirstLine + "[" + title + "]"
    newTitle = admonishBlock.replace(firstLine, newFirstLine)

    # Replace ` with :
    newBlock = (re.sub(backtickPattern, ":::", newTitle))

    stringFile = stringFile.replace(admonishBlock, newBlock)
    return stringFile

convert_admonish_blocks(common.testFile)