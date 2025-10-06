import shutil
import os
import sys
from copystatic import copy_files
from generate_page import generate_pages_recursive

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("Deleting content of public directory...")
    if os.path.exists("./docs"):
        shutil.rmtree("./docs")

    print("Copying files from static to public directory...")
    copy_files("./static", "./docs")

    generate_pages_recursive("./content", "./template.html", "./docs", basepath)


if __name__ =="__main__":
    main()