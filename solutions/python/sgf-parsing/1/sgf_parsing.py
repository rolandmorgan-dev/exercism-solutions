import re

class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        return (self.properties == other.properties and
                self.children == other.children)

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    if not input_string:
        raise ValueError("tree missing")

    index = 0
    length = len(input_string)

    def parse_tree():
        nonlocal index
        if input_string[index] != '(':
            raise ValueError("tree missing")
        index += 1

        nodes = []
        while index < length and input_string[index] != ')':
            if input_string[index] == ';':
                index += 1
                nodes.append(parse_node())
            elif input_string[index] == '(':
                child = parse_tree()
                if not nodes:
                    raise ValueError("tree with no nodes")
                nodes[-1].children.append(child)
            else:
                raise ValueError("tree missing")

        if not nodes:
            raise ValueError("tree with no nodes")
        if index >= length or input_string[index] != ')':
            raise ValueError("tree missing")
        index += 1

        for i in range(len(nodes) - 1):
            nodes[i].children = [nodes[i + 1]]
        return nodes[0]

    def parse_node():
        nonlocal index
        properties = {}

        while index < length and input_string[index] not in ';()':
            match = re.match(r'[A-Za-z]+', input_string[index:])
            if not match:
                break
            key = match.group(0)
            if not key.isupper():
                raise ValueError("property must be in uppercase")
            index += len(key)

            values = []
            if index >= length or input_string[index] != '[':
                raise ValueError("properties without delimiter")

            while index < length and input_string[index] == '[':
                index += 1
                val = ''
                while index < length:
                    c = input_string[index]
                    if c == ']':
                        index += 1
                        break
                    elif c == '\\':
                        index += 1
                        if index < length:
                            next_c = input_string[index]
                            if next_c == '\n':
                                pass  # remove escaped newline
                            elif next_c in '\t ':
                                val += ' '
                            else:
                                val += next_c
                            index += 1
                    else:
                        val += ' ' if c in '\t' else c
                        index += 1
                values.append(val)

            if key in properties:
                properties[key].extend(values)
            else:
                properties[key] = values

        return SgfTree(properties)

    tree = parse_tree()

    if index != length:
        raise ValueError("tree missing")

    return tree
