from pathlib import Path

testFilePath = Path(__file__).parent / "./testfile.md"

def read_file(filePath):
    with open(filePath, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def write_file(filePath, content):
    with open(filePath, 'w', encoding='utf-8') as file:
        file.write(content)

testFile = read_file(testFilePath)
print(testFilePath)