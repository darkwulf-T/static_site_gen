import shutil
import os
from copystatic import copy_files
from generate_page import generate_pages_recursive

def main():
    print("Deleting content of public directory...")
    if os.path.exists("./public"):
        shutil.rmtree("./public")

    print("Copying files from static to public directory...")
    copy_files("./static", "./public")

    generate_pages_recursive("./content", "./template.html", "./public")


if __name__ =="__main__":
    main()