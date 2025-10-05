import unittest
from markdown_blocks import markdown_to_block, BlockType, block_to_block_type


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_block(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_block(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type1(self):
        block = """
```
This is code
```
"""
        self.assertEqual(BlockType.CODE, block_to_block_type(block))

    def test_block_to_block_type2(self):
        block = "###Heading"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))
    
    def test_block_to_block_type3(self):
        block = """
> Quote 1
> Quote 2
"""
        self.assertEqual(BlockType.QUOTE, block_to_block_type(block))

    def test_block_to_block_type4(self):
        block = """
- item 1
- item 2
- item 3
"""
        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(block))

    def test_block_to_block_type5(self):
        block = """
1. item 1
2. item 2
3. item 3
"""
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(block))


if __name__ == "__main__":
    unittest.main()