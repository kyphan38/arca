import re


def check_structure(lines):
  errors = []

  found_h1 = False
  in_code_block = False

  heading_pattern = re.compile(r'^(#{1,6})\s+(.*)')
  code_fence_pattern = re.compile(r'^\s*```')

  for i, line in enumerate(lines):
    line_num = i + 1
    content = line.strip()

    # Track code blocks
    if code_fence_pattern.match(line):
      in_code_block = not in_code_block
      continue

    # Skip processing lines inside code blocks
    if in_code_block:
      continue

    if not content:
      continue

    match = heading_pattern.match(line)
    if not match:
      continue

    level = len(match.group(1))

    # Rule: Max heading depth is H3
    if level > 3:
      errors.append(f"Line {line_num}: H{level} is too deep - max depth is H3")

    # Rule: Only one H1 allowed
    if level == 1:
      if found_h1:
        errors.append(f"Line {line_num}: Multiple H1 found - only one H1 allowed per file")
      found_h1 = True

  return errors

