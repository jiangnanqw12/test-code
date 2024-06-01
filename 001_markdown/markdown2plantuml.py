import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension
from xml.etree.ElementTree import Element

class MarkdownToPlantUML(Treeprocessor):
    def __init__(self, md):
        super().__init__(md)
        self.uml = "@startmindmap\n"

    def run(self, root):
        self.parse_element(root, 1)
        self.uml += "@endmindmap\n"
        # Return the original root to comply with the expected return type
        return root

    def parse_element(self, element, level):
        for child in element:
            if child.tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                self.uml += f"* {child.text}\n"
            elif child.tag == 'ul':
                self.parse_list(child, level)

    def parse_list(self, ul, level):
        for li in ul:
            for sub in li:
                if sub.tag == 'p':
                    self.uml += f"{' ' * level}* {sub.text}\n"
                elif sub.tag == 'ul':
                    self.parse_list(sub, level + 1)

class PlantUMLExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(MarkdownToPlantUML(md), 'markdown_to_plantuml', 25)

def markdown_to_plantuml(md_text):
    md = markdown.Markdown(extensions=[PlantUMLExtension()])
    md.convert(md_text)
    # Access the UML code generated by the processor
    return md.treeprocessors['markdown_to_plantuml'].uml

# 示例 Markdown 文本
md_text = """
## test
- 1
  - 2
"""

# 转换并打印 PlantUML 代码
plantuml_code = markdown_to_plantuml(md_text)
print(plantuml_code)
