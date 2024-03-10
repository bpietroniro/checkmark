import pdftotext
import re
from mistune.renderers.markdown import MarkdownRenderer as MDR
from mistune import create_markdown

format_markdown = create_markdown(renderer=MDR(), plugins=['task_lists'])

TODO_PREFIX = r'- [ ] '

def process_and_print(filepath, start_page, end_page):
  def replacer(match):
    return match.group(1) + TODO_PREFIX
  
  with open(filepath, "rb") as f:
    pdf = pdftotext.PDF(f, physical=True)

  for pagenum in range(start_page, end_page):
    page = pdf[pagenum - 1]
    page = re.sub("\.{4,}", "", page)
    page = re.sub("\d+\n", "\n", page)
    page = re.sub("^(\s*)", replacer, page, flags=re.MULTILINE)
    md = format_markdown(page)
    with open("output.md", "w", encoding="utf-8") as f:
      f.write(md)

process_and_print("./example_inputs/GitNotesForProfessionals.pdf", 2, 3)