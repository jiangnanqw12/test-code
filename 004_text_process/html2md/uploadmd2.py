from notion.client import NotionClient
from notion.block import PageBlock
from md2notion.upload import upload
# new branch fix this
# Follow the instructions at https://github.com/jamalex/notion-py#quickstart to setup Notion.py
client = NotionClient(
    token_v2="ed90cc2412d13d4ca3ce7d2028c071c0c3d9a2e76765a70a3083ea14351005b3657c7cb39584c4679cab58d65c3dd6b14987d5b74c19826b69447fe8bbb3568b5740dfc03d0e144f816792387fe2")
page = client.get_block(
    "https://www.notion.so/2-e1fdda21b5c24348a292a440eba37871")

with open("output04 Student Services.md", "r", encoding="utf-8") as mdFile:
    newPage = page.children.add_new(PageBlock, title="TestMarkdown Upload")
    # Appends the converted contents of TestMarkdown.md to newPage
    upload(mdFile, newPage)
