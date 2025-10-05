from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def markdown_to_block(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    count = 0
    for char in block.strip("\n"):
        if char != "#":
            break
        count += 1
    if count < len(block):
        if 0 < count <= 6 and block.strip("\n")[count] == " " and block[count+1:].strip():
            return BlockType.HEADING
    if block.strip("\n").startswith("```") and block.strip("\n").endswith("```"):
        return BlockType.CODE
    lines = block.strip("\n").splitlines()
    check = True
    for line in lines:
        if not line.startswith(">"):
            check = False
    if check:
        return BlockType.QUOTE
    check = True
    for line in lines:
        if not line.startswith("-"):
            check = False
    if check:
        return BlockType.UNORDERED_LIST
    check = True
    i = 1
    for line in lines:
        if not line.startswith(f"{i}. "):
            check = False
        i += 1
    if check:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
    