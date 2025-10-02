import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a test", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a test", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)
    
    def test_eq3(self):
        node = TextNode("This is a test", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a test", TextType.ITALIC, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_eq4(self):
        node = TextNode("This is a test", TextType.BOLD)
        node2 = TextNode("This is a test", TextType.BOLD, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_eq5(self):
        node = TextNode("This is not a test", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a test", TextType.ITALIC, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text2(self):
        node = TextNode("This is a text node", "Plain_Text")
        with self.assertRaisesRegex(Exception, "Text type of the given text node is not supported"):
            text_node_to_html_node(node)

    def test_text3(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})


if __name__ == "__main__":
    unittest.main()