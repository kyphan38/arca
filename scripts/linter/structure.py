import re
from .config import ALLOWED_TITLES

def check_structure(lines):
  errors = []
  
  # 1. Progress
  found_h1 = False
  found_first_h2 = False
  has_valid_progress = False

  # 2. H2/H3 Structure
  curr_h2_text = None
  is_custom_h2 = False
  has_valid_child = False
  has_any_child = False

  # 3. Bridge Sentence Check
  last_seen_heading_level = 0 

  # --- Regex patterns ---
  heading_pattern = re.compile(r'^(#{1,3})\s+(.*)')
  progress_pattern = re.compile(r'^\s*-\s*\[\s*[xX ]?\s*\]\s*Progress:\s*', re.IGNORECASE)
  bullet_pattern = re.compile(r'^\s*[-*]\s+')

  for i, line in enumerate(lines):
    line_num = i + 1
    content = line.strip()

    if not content:
      continue

    # Check 1: No bullet after H2/H3
    is_bullet = bullet_pattern.match(line)
    
    if is_bullet:
      if last_seen_heading_level in [2, 3]:
        errors.append(f"Line {line_num}: Abrupt transition! Bullet point found immediately after H{last_seen_heading_level}. Add a bridge sentence")
    
    # Check 2: Progress line
    if progress_pattern.match(line):
      if not found_h1:
        errors.append(f"Line {line_num}: 'Progress' found before H1 heading")
      elif found_first_h2:
        pass
      else:
        has_valid_progress = True
      
      last_seen_heading_level = 0
      continue

    # Check 3: Headings
    match = heading_pattern.match(line)
    if match:
      level = len(match.group(1))
      text = match.group(2).strip()

      last_seen_heading_level = level

      # H1
      if level == 1:
        found_h1 = True
        if not text.islower():
          errors.append(f"Line {line_num}: H1 heading must be lowercase: '# {text}'")
        continue
      
      # H2
      if level == 2:
        if not found_first_h2:
          found_first_h2 = True
          if not has_valid_progress:
            errors.append(f"Line {line_num}: Missing '- [ ] Progress: ...' line before the first H2")

        # Check previous H2 structure
        if curr_h2_text and is_custom_h2:
          if not has_any_child:
            errors.append(f"Line {line_num}: Custom H2 '{curr_h2_text}' must have at least one child H3 heading")
          elif not has_valid_child:
            errors.append(f"Line {line_num}: Custom H2 '{curr_h2_text}' must have at least one valid child H3 heading")

        # Setup new H2
        curr_h2_text = text
        has_any_child = False
        has_valid_child = False

        is_standard = any(k.lower() in text.lower() for k in ALLOWED_TITLES)
        is_custom_h2 = not is_standard

      # H3
      elif level == 3:
        if is_custom_h2:
          has_any_child = True
          is_standard_h3 = any(k.lower() in text.lower() for k in ALLOWED_TITLES)
          if is_standard_h3:
            has_valid_child = True
    
    else:
      last_seen_heading_level = 0

  # Final check
  if curr_h2_text and is_custom_h2:
    if not has_any_child:
      errors.append(f"End of file: Custom H2 '{curr_h2_text}' must have at least one child H3 heading")
    elif not has_valid_child:
      errors.append(f"End of file: Custom H2 '{curr_h2_text}' must have at least one valid child H3 heading")

  return errors