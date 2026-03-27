import re
from .config import ALLOWED_TITLES


def check_structure(lines):
  errors = []

  found_h1 = False
  has_valid_progress = False

  heading_pattern = re.compile(r'^(#{1,6})\s+(.*)')
  progress_pattern = re.compile(r'^\s*-\s*\[\s*[xX ]?\s*\]\s*Progress:\s*(Draft|Review|Done)\s*$', re.IGNORECASE)

  for i, line in enumerate(lines):
    line_num = i + 1
    content = line.strip()

    if not content:
      continue

    # Check: Progress line
    if progress_pattern.match(line):
      if not found_h1:
        errors.append(f"Line {line_num}: 'Progress' line found before H1")
      else:
        has_valid_progress = True
      continue

    match = heading_pattern.match(line)
    if not match:
      continue

    level = len(match.group(1))
    text = match.group(2).strip()

    # Rule: Max heading depth is H3
    if level > 3:
      errors.append(f"Line {line_num}: H{level} is too deep — max depth is H3")

    # Rule: H1 must be all lowercase, only one allowed
    if level == 1:
      if found_h1:
        errors.append(f"Line {line_num}: Multiple H1 found — only one H1 allowed per file")
      else:
        found_h1 = True
        if not text.islower():
          errors.append(f"Line {line_num}: H1 must be all lowercase — got '# {text}'")

    # Rule: H2/H3 must start with uppercase
    if level in [2, 3]:
      if text and not text.startswith('`'):
        if text[0].islower():
          errors.append(f"Line {line_num}: H{level} must start with uppercase — got '{'#' * level} {text}'")

    # Rule: H3 must be from ALLOWED_TITLES (except when under Review Questions)
    if level == 3:
      if text not in ALLOWED_TITLES:
        errors.append(f"Line {line_num}: H3 '{text}' is not in allowed H3 titles. Must be one of: {', '.join(ALLOWED_TITLES)}")

  # Rule: Progress line must exist
  if found_h1 and not has_valid_progress:
    errors.append("Missing '- [ ] Progress: Draft/Review/Done' after H1")

  return errors
