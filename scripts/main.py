import os
import sys
import re

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from linter.structure import check_structure

DOCS_DIR = "docs"
KEBAB_CASE_PATTERN = re.compile(r'^[0-9a-z-]+$')
IGNORE_DIRS = {".docusaurus", "node_modules", "img", ".git", ".gemini"}

def check_naming(name, is_dir=False):
    # Strip extension for files
    base_name = name if is_dir else os.path.splitext(name)[0]
    if not KEBAB_CASE_PATTERN.match(base_name):
        return False
    return True

def main():
    print(f"Starting linter on directory: {DOCS_DIR} ...\n")
    has_error = False

    for root, dirs, files in os.walk(DOCS_DIR, topdown=True):
        # Filter out ignored directories so we don't walk into them
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        # 1. Check folder names
        for d in dirs:
            if not check_naming(d, is_dir=True):
                has_error = True
                print(f"Naming Error: Folder '{d}' in '{root}' is not kebab-case (lowercase, no spaces)")

        # 2. Check files
        for file in files:
            if not file.endswith(".md"):
                continue

            # Check file name
            if not check_naming(file, is_dir=False):
                has_error = True
                print(f"Naming Error: File '{file}' in '{root}' is not kebab-case (lowercase, no spaces)")

            filepath = os.path.join(root, file)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
            except Exception as e:
                print(f"Cannot read file {filepath}: {e}")
                continue

            # 3. Check Markdown structure
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