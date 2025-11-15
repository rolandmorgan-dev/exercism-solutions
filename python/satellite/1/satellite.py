def tree_from_traversals(preorder :list, inorder :list) -> dict:
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")

    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")

    if len(preorder) != len(set(preorder)):
        raise ValueError("traversals must contain unique items")

    # Call the recursive helper to build a tree as a nested dictionary
    return _rebuild_tree(preorder, inorder)


def _rebuild_tree(preorder, inorder):
    # Base case: if preorder or inorder is empty, return empty dict
    if not preorder or not inorder:
        return {}

    # Root
    root = preorder[0]
    root_index = inorder.index(root)

    # Left subtree:
    left_inorder = inorder[:root_index]
    left_preorder = preorder[1:1 + root_index]

    # Right subtree:
    right_inorder = inorder[1 + root_index:]
    right_preorder = preorder[1 + root_index:]

    return {"v": root,
            "l": _rebuild_tree(left_preorder, left_inorder),
            "r": _rebuild_tree(right_preorder, right_inorder)}
