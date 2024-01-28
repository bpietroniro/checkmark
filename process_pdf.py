import pdftotext
import re

TODO_PREFIX = r'- [ ] '

def process_and_print(filepath, start_page, end_page):
  def replacer(match):
    return match.group(1) + TODO_PREFIX
  
  with open(filepath, "rb") as f:
    pdf = pdftotext.PDF(f, physical=True)

  for pagenum in range(start_page, end_page):
    page = pdf[pagenum - 1]
    page = re.sub("\.\.\.\.+", "", page)
    page = re.sub("\d+\n", "\n", page)
    page = re.sub("^(\s*)", replacer, page, flags=re.MULTILINE)
    print(page)

process_and_print("./example_inputs/GitNotesForProfessionals.pdf", 2, 3)