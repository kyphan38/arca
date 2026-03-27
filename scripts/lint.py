import os
import sys
import re

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from linter.structure import check_structure

DOCS_DIR = "docs"
KEBAB_CASE_PATTERN = re.compile(r'^[0-9a-z-]+$')
IGNORE_DIRS = {".docusaurus", "node_modules", "img", ".git", ".gemini"}


def check_naming(name, is_dir=False):
  base_name = name if is_dir else os.path.splitext(name)[0]
  return bool(KEBAB_CASE_PATTERN.match(base_name))


def main():
  print(f"Starting linter on: {DOCS_DIR}\n")
  has_error = False

  for root, dirs, files in os.walk(DOCS_DIR, topdown=True):
    dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

    # Check folder names
    for d in dirs:
      if not check_naming(d, is_dir=True):
        has_error = True
        print(f"Naming Error: '{d}' in '{root}' — folders must be kebab-case, no spaces")

    # Check markdown files
    for file in files:
      if not file.endswith(".md"):
        continue

      if not check_naming(file, is_dir=False):
        has_error = True
        print(f"Naming Error: '{file}' in '{root}' — files must be kebab-case, no spaces")

      filepath = os.path.join(root, file)

      try:
        with open(filepath, "r", encoding="utf-8") as f:
          lines = f.readlines()
      except Exception as e:
        print(f"Cannot read {filepath}: {e}")
        continue

      # Skip structure check for index.md files
      if file == "index.md":
        continue

      structure_errors = check_structure(lines)

      if structure_errors:
        has_error = True
        print(f"Errors in: {filepath}")
        for error in structure_errors:
          print(f"  - {error}")
        print("-" * 40)

  if has_error:
    print("\nLINT FAILED — fix errors above")
    sys.exit(1)
  else:
    print("\nLINT PASSED — all docs look good")
    sys.exit(0)


if __name__ == "__main__":
  main()
