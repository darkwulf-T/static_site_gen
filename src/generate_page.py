from markdown_to_html_node_file import markdown_to_html_node
import os
from pathlib import Path

def extract_title(markdown):
    header = None
    lines = markdown.split("\n")
    for line in lines:
        if line.strip().startswith("#"):
            header = line.strip("# ")
            break
    if header == None:
        raise Exception("no h1 header in markdown")
    return header


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        source = f.read()
    with open(template_path) as f:
        template = f.read()
    html_node = markdown_to_html_node(source)
    html_string = html_node.to_html()
    title = extract_title(source)
    final_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    
    dirpath = os.path.dirname(dest_path)
    os.makedirs(dirpath, exist_ok=True)
    with open(dest_path, mode="w") as f:
        f.write(final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for file in os.listdir(dir_path_content):
        source = os.path.join(dir_path_content, file)
        destination = os.path.join(dest_dir_path, file)
        if os.path.isfile(source):
            dest_path = Path(destination).with_suffix(".html")
            generate_page(source, template_path, dest_path)
        else:
            generate_pages_recursive(source, template_path, destination)