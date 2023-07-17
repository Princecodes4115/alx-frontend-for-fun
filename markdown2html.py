#!/usr/bin/python3

import sys
import markdown

def main():
  if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html")
    sys.exit(1)

  markdown_file = sys.argv[1]
  html_file = sys.argv[2]

  if not os.path.exists(markdown_file):
    print("Missing {}.".format(markdown_file))
    sys.exit(1)

  with open(markdown_file, "r") as f:
    markdown_content = f.read()

  html_content = markdown.markdown(markdown_content)

  with open(html_file, "w") as f:
    f.write(html_content)

if __name__ == "__main__":
  main()

