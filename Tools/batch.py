from pathlib import Path
import common
import convert_admonish
import convert_tabs
import convert_hr
import remove_p
import fix_details

targetDirectory = Path(__file__).parent / "../docs"

def get_files(path: Path):
    files = []
    for item in Path.iterdir(path):
        if item.is_file():
            files.append(item)
        elif item.is_dir():
            recursive = get_files(item)
            for r in recursive:
                files.append(r)
    return files

allFiles = get_files(targetDirectory)

for file in allFiles:
    print("Reading "+str(file)+ "...")
    stringFile = common.read_file(file)

    # Check for admonish.
    admonitions = convert_admonish.has_admonish(stringFile)
    if admonitions > 0:
        print(str(admonitions) +" admonitions found.")
        stringFile = convert_admonish.convert_admonish_blocks(stringFile)

    # Check for tabs.
    tabs = convert_tabs.has_block(stringFile)
    if tabs > 0:
        print(str(tabs) +" tabs found.")
        #stringFile = convert_tabs.convert_tabs(stringFile)

    # Check for <hr> block.
    hr = convert_hr.has_hr(stringFile)
    if hr > 0:
        print (str(hr) + " <hr> blocks found.")
        stringFile = convert_hr.convert_hr(stringFile)

    # Check for <p> block.
    p = remove_p.has_p(stringFile)
    if p > 0:
        print (str(p) + " <p> blocks found.")
        stringFile = remove_p.remove_p(stringFile)

    # Check for <details><summary> with no newline.
    details = fix_details.has_details(stringFile)
    if details > 0:
        print (str(details) + " <details><summary> blocks found.")
        stringFile = fix_details.fix_details(stringFile)
    
    common.write_file(file, stringFile)