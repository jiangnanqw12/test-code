import io
import os.path
import glob
from pathlib import Path
from notion.block import PageBlock
from notion.client import NotionClient
from md2notion.upload import upload

client = NotionClient(
    token_v2="ed90cc2412d13d4ca3ce7d2028c071c0c3d9a2e76765a70a3083ea14351005b3657c7cb39584c4679cab58d65c3dd6b14987d5b74c19826b69447fe8bbb3568b5740dfc03d0e144f816792387fe2")

page = client.get_block(
    "https://www.notion.so/e-4d886478e2644aa89d42d798fd7d046d")

for fp in glob.glob("*.md", recursive=True):
    with open(fp, "r", encoding="utf-8") as mdFile:
        # Preprocess the Markdown frontmatter into yaml code fences
        mdStr = mdFile.read()
        mdChunks = mdStr.split("---")
        mdStr = \
            f"""```yaml
{mdChunks[1]}
`` `

{'---'.join(mdChunks[2:])}
"""
        mdFile = io.StringIO(mdStr)
        mdFile.__dict__["name"] = fp  # Set this so we can resolve images later

        pageName = os.path.basename(fp)[:40]
        newPage = page.children.add_new(PageBlock, title=pageName)
        print(f"Uploading {fp} to Notion.so at page {pageName}")
        # Get the image relative to the markdown file in the flavor that Hexo
        # stores its images (in a folder with the same name as the md file)

        def convertImagePath(imagePath, mdFilePath):
            return Path(mdFilePath).parent / Path(mdFilePath).stem / Path(imagePath)
        upload(mdFile, newPage, imagePathFunc=convertImagePath)
