from __future__ import annotations
from json import dumps


class Tree:
    def __init__(self, label: str, children: list[Tree] | None = None) -> None:
        self.label = label
        self.children = children or []

    def __dict__(self) -> dict[str, list[dict]]:
        return {self.label: [child.__dict__() for child in sorted(self.children)]}

    def __str__(self, indent: int | None = None) -> str:
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other: Tree) -> bool:
        return self.label < other.label

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Tree):
            return NotImplemented
        return self.__dict__() == other.__dict__()

    def _node_search(self, label: str) -> list[Tree] | None:
        """
        Return a path from the current node to the node with the given label.
        Return None if no such node exists.
        """
        if self.label == label:
            return [self]

        for child in self.children:
            path = child._node_search(label)
            if path:
                return [self] + path

        return None

    def from_pov(self, from_node: str) -> Tree:
        """Reorient the tree so that the node with from_node becomes the root."""
        path = self._node_search(from_node)
        if path is None:
            raise ValueError("Tree could not be reoriented")

        if len(path) == 1:
            return path[0]

        # Reverse parent-child links along the path to re-root
        for parent, child in zip(path, path[1:]):
            parent.children.remove(child)
            child.children.append(parent)

        return path[-1]

    def path_to(self, from_node: str, to_node: str) -> list[str]:
        """Return the path as labels from from_node to to_node."""
        rerooted = self.from_pov(from_node)
        path = rerooted._node_search(to_node)

        if path is None:
            raise ValueError("No path found")

        return [node.label for node in path]
