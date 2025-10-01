import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="p", value="This is a paragraph", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_printing(self):
        node = HTMLNode(tag="p", value="This is a paragraph")
        self.assertEqual(repr(node), "p, This is a paragraph, None, None")
        