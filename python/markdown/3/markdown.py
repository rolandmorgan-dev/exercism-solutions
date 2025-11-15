import re

# Add HTML formatting tags to a string based on markdown-like syntax
def parse(text : str) -> str:
    # Headers
    for i in range(6, 0, -1):
        text = re.sub(fr"^ *{'#' * i} (.*\S)", fr"<h{i}>\1</h{i}>", text, flags=re.M)
    
    # Bolds & Italics
    text = re.sub("__(.+?)__", r"<strong>\1</strong>", text)
    text = re.sub("_(.+?)_", r"<em>\1</em>", text)
    
    # Lists
    text = re.sub(r"^\* *(.*\S)", r"<li>\1</li>", text, flags=re.M)
    text = re.sub(r"(<li>.*</li>)", r"<ul>\1</ul>", text, flags=re.S)
    
    # Paragraphs
    text = re.sub("^(?!<[hul])(.*\S)\w*", r"<p>\1</p>", text, flags=re.M)
    
    return text.replace("\n", "")