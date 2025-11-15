from copy import deepcopy

class Zipper:
    def __init__(self, focus, context):
        self.focus = focus
        self.context = context

    @staticmethod
    def from_tree(tree):
        return Zipper(tree, [])

    def value(self):
        return self.focus["value"]

    def set_value(self, value):
        new_focus = deepcopy(self.focus)
        new_focus["value"] = value
        return Zipper(new_focus, self.context)

    def left(self):
        if self.focus["left"] is None:
            return None
        new_context = self.context + [(None, self.focus["value"], self.focus["right"], True)]
        return Zipper(self.focus["left"], new_context)

    def right(self):
        if self.focus["right"] is None:
            return None
        new_context = self.context + [(self.focus["left"], self.focus["value"], None, False)]
        return Zipper(self.focus["right"], new_context)

    def up(self):
        if not self.context:
            return None
        left_sib, parent_val, right_sib, is_left = self.context[-1]
        new_context = self.context[:-1]
        if is_left:
            new_focus = {
                "value": parent_val,
                "left": self.focus,
                "right": right_sib,
            }
        else:
            new_focus = {
                "value": parent_val,
                "left": left_sib,
                "right": self.focus,
            }
        return Zipper(new_focus, new_context)

    def set_left(self, subtree):
        new_focus = deepcopy(self.focus)
        new_focus["left"] = subtree
        return Zipper(new_focus, self.context)

    def set_right(self, subtree):
        new_focus = deepcopy(self.focus)
        new_focus["right"] = subtree
        return Zipper(new_focus, self.context)

    def to_tree(self):
        current = self
        while current.context:
            current = current.up()
        return current.focus