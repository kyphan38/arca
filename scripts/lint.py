import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from linter.structure import check_structure
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = "docs"

def main():
  print(f"Starting linter on directory: {DOCS_DIR} ...\n")
  has_error = False

  for root, dirs, files in os.walk(DOCS_DIR, topdown=True):
    for file in files:
      if file.endswith(".md"):
        filepath = os.path.join(root, file)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            print(f"Cannot read file {filepath}: {e}")
            continue

        structure_errors = check_structure(lines)

        if structure_errors:
          has_error = True
          print(f"Errors in file: {filepath}")
          for error in structure_errors:
            print(f"  - {error}")
          print("-" * 30)
        
  if has_error:
      print("\nLINT FAILED: Please fix the errors above")
      sys.exit(1)
  else:
      print("\nLINT PASSED: All docs look good")
      sys.exit(0)

if __name__=="__main__":
  main()