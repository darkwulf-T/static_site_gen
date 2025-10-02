import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="p", value="This is a paragraph", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_printing(self):
        node = HTMLNode(tag="p", value="This is a paragraph")
        self.assertEqual(repr(node), "p, This is a paragraph, None, None")


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_props_empty(self):
        node = LeafNode("a", "Click me!", {})
        self.assertEqual(node.to_html(), '<a>Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode("p", None)
        with self.assertRaisesRegex(ValueError, "LeafNode must have a value"):
            node.to_html()

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_children_props(self):
        child_node = LeafNode("span", "hi")
        parent_node = ParentNode("div", [child_node], {"class": "box", "id": "a1"})
        self.assertEqual(parent_node.to_html(), '<div class="box" id="a1"><span>hi</span></div>')

    def test_to_html_with_children_props2(self):
        child_node = LeafNode("span", "hi", {"target": "_blank"})
        parent_node = ParentNode("div", [child_node], {"class": "box", "id": "a1"})
        self.assertEqual(parent_node.to_html(), '<div class="box" id="a1"><span target="_blank">hi</span></div>')

    def test_to_html_with_children_props3(self):
        child_node = LeafNode("span", "hi", {"target": "_blank"})
        child_node2 = LeafNode("p", "Hello, world!")
        child_node3 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        parent_node = ParentNode("div", [child_node, child_node2, child_node3], {"class": "box", "id": "a1"})
        self.assertEqual(parent_node.to_html(), '<div class="box" id="a1"><span target="_blank">hi</span><p>Hello, world!</p><a href="https://www.google.com">Click me!</a></div>')
        
    def test_no_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaisesRegex(ValueError, "ParentNode must have children"):
            parent_node.to_html()

    def test_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaisesRegex(ValueError, "ParentNode must have a tag"):
            parent_node.to_html()

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )





        if __name__ == "__main__":
            unittest.main()