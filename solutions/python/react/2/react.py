class Cell(object):
    def __init__(self, initial_value):
        self._value = initial_value
        self.listeners = set()

    @property
    def value(self):
        return self._value

    def notify_listeners(self, compare_vals):
        for listener in self.listeners:
            listener(compare_vals)


class InputCell(Cell):
    @Cell.value.setter
    def value(self, new_value):
        if new_value != self._value:
            self._value = new_value
            compare_vals = {}
            self.notify_listeners(compare_vals)
            for cell, old_value in compare_vals.items():
                if cell.value != old_value:
                    cell.trigger_callbacks()


class ComputeCell(Cell):
    def __init__(self, cells, compute_function):
        self.cells = cells
        self.compute_function = compute_function
        self._value = self.compute()
        
        self.listeners = set()
        self.callbacks = set()

        for cell in self.cells:
            cell.listeners.add(self.update)
    
    def compute(self):
        return self.compute_function([c.value for c in self.cells])

    def update(self, compare_vals):
        new_value = self.compute()
        if new_value != self.value:
            compare_vals.setdefault(self, self.value)
            self._value = new_value
            self.notify_listeners(compare_vals)

    def add_callback(self, callback):
        self.callbacks.add(callback)

    def remove_callback(self, callback):
        self.callbacks.discard(callback)
    
    def trigger_callbacks(self):
        for cb in self.callbacks:
            cb(self.value)