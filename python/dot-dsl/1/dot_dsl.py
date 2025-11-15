NODE, EDGE, ATTR = range(3)


class Node:
    """Represents a graph node with a name and associated attributes."""
    def __init__(self, name: str, attrs: dict):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    """Represents a directed edge between two nodes with attributes."""
    def __init__(self, src: str, dst: str, attrs: dict):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    """Graph structure built from a list of DSL tuples."""
    def __init__(self, data: list[tuple] = None):
        # Validates input before attempting to build the graph
        self.handle_errors(data)

        self.nodes = []
        self.edges = []
        self.attrs = {}

        # Build graph from DSL if data is provided
        if data: self.build_graph(data)

    def build_graph(self, data: list[tuple]):
        """
        Parses the list of tuples (DSL) and populates nodes, edges, and attributes.
        Each tuple starts with a type identifier (NODE, EDGE, ATTR).
        """
        for item in data:
            item_type, *details = item

            if item_type == NODE:
                name, attrs = details
                self.nodes.append(Node(name, attrs))
            elif item_type == EDGE:
                src, dst, attrs = details
                self.edges.append(Edge(src, dst, attrs))
            elif item_type == ATTR:
                name, attrs = details
                self.attrs[name] = attrs

    def handle_errors(self, data: list[tuple]):
        """
        Validates the input list of DSL tuples, ensuring each item is well-formed
        Raises appropriate exception messages for malformed or invalid items.
        """
        if data is None: return

        # Graph input must be a list of tuples
        if not isinstance(data, list) or not all(isinstance(x, tuple) for x in data):
            raise TypeError("Graph data malformed")

        dsl_item_lengths = {NODE: 3, EDGE: 4, ATTR: 3}

        for item in data:
            # Catch tuples that are too short or too long
            if len(item) < 3 or 4 < len(item):
                raise TypeError("Graph item incomplete")

            item_type = item[0]

            # Check for unknown DSL item types
            if item_type not in dsl_item_lengths:
                raise ValueError("Unknown item")

            # Check for incorrect tuple length for the given item type
            if len(item) != dsl_item_lengths[item_type]:
                item_name = ("Node", "Edge", "Attribute")[item_type]
                raise ValueError(f"{item_name} is malformed")