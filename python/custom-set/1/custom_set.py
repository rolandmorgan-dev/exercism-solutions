class CustomSet:
    def __init__(self, elements=[]):
        seen = set()
        self.elements = [e for e in elements if not (e in seen or seen.add(e))]

    def isempty(self):
        return not self.elements

    def __contains__(self, element):
        return element in self.elements

    def __eq__(self, other):
        return set(self.elements) == set(other.elements)

    def __len__(self):
        return len(self.elements)

    def add(self, element):
        if element not in self.elements: self.elements.append(element)

    def issubset(self, other):
        return all(elem in other.elements for elem in self.elements)

    def isdisjoint(self, other):
        return all(elem not in other.elements for elem in self.elements)

    def intersection(self, other):
        return CustomSet([e for e in self.elements if e in other.elements])

    def __sub__(self, other):
        return CustomSet([e for e in self.elements if e not in other.elements])

    def __add__(self, other):
        return CustomSet(list(set(self.elements + other.elements)))