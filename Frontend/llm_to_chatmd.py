import sys
import re
import argparse

def unescape_text(text):
    r"""
    Unescape common escapes: \n, \", \', \`, \\
    """
    def replace_match(match):
        char = match.group(1)
        if char == 'n': return '\n'
        if char == '"': return '"'
        if char == "'": return "'"
        if char == '`': return '`'
        if char == '\\': return '\\'
        return match.group(0) # Keep as is if not a standard escape
    
    return re.sub(r'\\(.)', replace_match, text)

def process_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to capture code blocks: ```...```
    # We use re.DOTALL so . matches newlines (if any exist), 
    # but primarily this works on the raw string even if it's one line.
    parts = re.split(r'(```.*?```)', content, flags=re.DOTALL)
    
    processed_parts = []
    for part in parts:
        if part.startswith('```') and part.endswith('```'):
            # Code block: Only fix newlines to restore structure
            # Do NOT unescape quotes etc per user request
            processed_part = part.replace(r'\n', '\n')
            processed_parts.append(processed_part)
        else:
            # Text block: Full unescape
            processed_parts.append(unescape_text(part))
            
    final_output = ''.join(processed_parts)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert raw LLM text to Markdown")
    parser.add_argument("input", help="Input raw file")
    parser.add_argument("output", help="Output markdown file")
    args = parser.parse_args()
    
    process_file(args.input, args.output)
