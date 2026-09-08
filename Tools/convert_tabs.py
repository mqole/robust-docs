import common
import re

startDetails = "<details>"
endDetails = "<\/details>"
startSummary = "<summary>"
endSummary = "<\/summary>"
contentPattern = "((\n|.)*?)"
linePattern = "(.*?)"
betweenTabPattern = "(\n| )*?"

# This is kind of awkward because the mdbook details tabs are formatted as dropdowns...
# buuuut whatever :-p tabs are generally nicer to look at anyway.
# if it starts to become a genuine formatting issue, I'll look into recreating the dropdown functionality.

def has_block(stringFile: str):
    n = re.findall(startDetails, stringFile)
    return len(n)

def convert_tabs(stringFile: str):
    currentSlice = stringFile
    currentFileIndex = 0
    tabItems = []

    for _ in range(has_block(stringFile)):
        block = get_block(currentSlice)
        tabItems.append(get_block_content(currentSlice))
        # Move onto the next slice.
        currentFileIndex += block.end()
        currentSlice = currentSlice[block.end():]
        if has_sibling_block(currentSlice):
            continue

        # No siblings, this is the end of our tab group.
        stringFile = amend_file(stringFile, tabItems, currentFileIndex)
        # Since we've amended the file, we need to reset the file index & slice.
        currentFileIndex = 0
        currentSlice = stringFile
        tabItems = []

    return stringFile

def amend_file(stringFile: str, tabItems: list, currentFileIndex: int,):
    oldBlockStart = get_block(stringFile).start()
    newBlock = format_tabs(tabItems)
    return stringFile[:oldBlockStart] + newBlock + stringFile[currentFileIndex:]

def format_tabs(tabItems: list):
    tabItemBlock = ""
    for n in tabItems:
        tabItemBlock = tabItemBlock + "\n<TabItem value =\"" + n[0] + "\">"
        tabItemBlock = tabItemBlock + n[1]
        tabItemBlock = tabItemBlock + "</TabItem>"
    return "<Tabs>" + tabItemBlock + "\n</Tabs>"

def get_block(stringFile: str):
    return re.search(startDetails + contentPattern + endDetails, stringFile)

# Grab a single dropdown. This will be one tab group.
def get_block_content(stringFile: str):
    block = get_block(stringFile).group()
    blockName = re.search(startSummary + linePattern + endSummary, block)
    
    blockRemovedName = block.replace(blockName.group(), "")
    blockContent = re.search(startDetails + contentPattern + endDetails, blockRemovedName).group(1)
    return [blockName.group(1), blockContent]

def has_sibling_block(slice: str):
    try:
        # First, find the location of our next details start block.
        # also make sure we include the actual details. This will be our end point.
        nextBlock = slice[:slice.index(startDetails) + len(startDetails)]
        # Make sure the blocks only have whitespace between them!
        assert re.match(betweenTabPattern + startDetails, nextBlock).group() is not None
        return True
    except:
        return False

convert_tabs(common.testFile)