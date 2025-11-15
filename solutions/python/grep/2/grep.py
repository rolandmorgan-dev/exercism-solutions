"""
Flags:
  -n : Prefix matching lines with line number (after filename if present)
  -l : Output only filenames with at least one matching line
  -i : Case-insensitive search
  -v : Invert match — select non-matching lines
  -x : Match only entire lines
"""

def grep(pattern, flags, files):
    # Parse flags
    flag_i = "-i" in flags
    flag_x = "-x" in flags
    flag_n = "-n" in flags
    flag_l = "-l" in flags
    flag_v = "-v" in flags
    
    # Case-insensitive pattern adjustment
    search_pattern = pattern.lower() if flag_i else pattern
    
    result = []
    for file in files:
        with open(file) as f:
            lines = f.readlines()
        
        matched_lines = []
        for idx, line in enumerate(lines):
            line_content = line.rstrip("\n")
            compare_line = line_content.lower() if flag_i else line_content
            
            # Determine match
            if flag_x:
                is_match = compare_line == search_pattern
            else:
                is_match = search_pattern in compare_line
            
            if flag_v:
                is_match = not is_match
            
            if is_match:
                if flag_l:
                    # Only list filename once if match is found
                    result.append(file + "\n")
                    break
                
                prefix = ""
                if len(files) > 1:
                    prefix += f"{file}:"
                if flag_n:
                    prefix += f"{idx + 1}:"
                result.append(prefix + line)
            
    return "".join(result)