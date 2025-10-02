class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None or not self.props:
            return ""
        final_string =""
        for att in sorted(self.props):
            final_string += " " + f'{att}="{str(self.props[att])}"'
        return final_string
    
    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, [], props)

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode must have a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def props_to_html(self):
        return super().props_to_html()
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None or not self.children:
            raise ValueError("ParentNode must have children")
        temp = ""
        for child in self.children:
            temp += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{temp}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"