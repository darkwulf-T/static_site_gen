import re
from textnode import TextType, TextNode, split_nodes_delimeter

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for nodes in old_nodes:
        if nodes.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(nodes)
            continue
        original_text = nodes.text
        images = extract_markdown_images(original_text)
        if not images:
            new_nodes.append(nodes)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAIN_TEXT))
    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    for nodes in old_nodes:
        if nodes.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(nodes)
            continue
        original_text = nodes.text
        links = extract_markdown_links(original_text)
        if not links:
            new_nodes.append(nodes)
            continue
        for link in links:
            section = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(section) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if section[0] != "":
                new_nodes.append(TextNode(section[0], TextType.PLAIN_TEXT))
            new_nodes.append(
                TextNode(
                    link[0],
                    TextType.LINK,
                    link[1]
                )
            )
            original_text = section[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAIN_TEXT))
    return new_nodes


def text_to_textnodes(text):
    new_nodes = []
    text_node = TextNode(text, TextType.PLAIN_TEXT)
    bold_ex = split_nodes_delimeter([text_node], "**", TextType.BOLD)
    italic_ex = split_nodes_delimeter(bold_ex, "_", TextType.ITALIC)
    code_ex = split_nodes_delimeter(italic_ex, "`", TextType.CODE)
    image_ex = split_nodes_image(code_ex)
    new_nodes.extend(split_nodes_links(image_ex))
    return new_nodes

def markdown_to_block(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks = []
    for block in blocks:
        cleaned_blocks.append(block.strip())
    final_blocks = []
    for block in cleaned_blocks:
        if block != "":
            final_blocks.append(block)
    return final_blocks