import unittest
from generate_page import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        header = extract_title("# Hello")
        self.assertEqual("Hello", header)

    def test_extract_title2(self):
        markdown = """
# Heading 1
## Heading 2
This is a paragraph of text
"""
        header = extract_title(markdown)
        self.assertEqual("Heading 1", header)