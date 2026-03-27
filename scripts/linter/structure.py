import re

def check_structure(lines):
    errors = []
    found_h1 = False
    has_valid_progress = False

    # Regex patterns
    heading_pattern = re.compile(r'^(#{1,6})\s+(.*)')
    progress_pattern = re.compile(r'^\s*-\s*\[\s*[xX ]?\s*\]\s*Progress:\s*(Draft|Review|Done)\s*$', re.IGNORECASE)

    for i, line in enumerate(lines):
        line_num = i + 1
        content = line.strip()

        if not content:
            continue

        # Check Progress line
        if progress_pattern.match(line):
            if not found_h1:
                errors.append(f"Line {line_num}: 'Progress' found before H1 heading")
            else:
                has_valid_progress = True
            continue

        # Check Headings
        match = heading_pattern.match(line)
        if match:
            level = len(match.group(1))
            text = match.group(2).strip()

            if level > 3:
                errors.append(f"Line {line_num}: Heading depth too deep (H{level}). Max depth is H3.")

            # H2 and H3 should be Title Case (Check if it starts with uppercase)
            if level in [2, 3]:
                if text and not text.startswith('`'):
                    if text[0].islower():
                        errors.append(f"Line {line_num}: H{level} should start with an uppercase letter: '{text}'")

            # H1 Rules
            if level == 1:
                if found_h1:
                    errors.append(f"Line {line_num}: Multiple H1 headings found. Only one H1 is allowed per file.")
                else:
                    found_h1 = True
                    if not text.islower():
                        errors.append(f"Line {line_num}: H1 heading must be lowercase: '# {text}'")

    # Final check
    if found_h1 and not has_valid_progress:
        errors.append("File is missing a valid '- [ ] Progress: [Draft/Review/Done]' line after H1")

    return errors