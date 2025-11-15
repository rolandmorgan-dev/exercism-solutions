import re

# Add HTML formatting tags to a string based on markdown-like syntax
def parse(text : str) -> str:
    # Header
    if text.startswith("#") and text.count("#", 0, 7) < 7:
        header = len(re.match("(#{1,6})", text).group(1))
        text = re.sub("#+ ?(.+)", fr"<h{header}>\1</h{header}>", text)
    
    # Bold & Italic
    text = re.sub("__(.+?)__", r"<strong>\1</strong>", text)
    text = re.sub("_(.+?)_", r"<em>\1</em>", text)
    
    # List
    text = re.sub(r"^\*\s?(.*)$", r"<li>\1</li>", text, flags=re.M)
    text = re.sub(r"(<li>.*</li>)", r"<ul>\1</ul>", text, flags=re.S)
    
    # Paragraph
    text = re.sub("^(?!<[hul])(.+)$", r"<p>\1</p>", text, flags=re.M)
    
    return text.replace("\n", "")