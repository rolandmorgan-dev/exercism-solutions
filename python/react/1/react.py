class Cell:
    def __init__(self):
        self._value = None
        self._dependents = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self.set_value(new_value)

    def set_value(self, new_value):
        if self._value != new_value:
            self._value = new_value
            changed = {}
            self._notify_dependents(changed)
            for cell, old_value in changed.items():
                if cell.value != old_value:
                    cell._trigger_callbacks()

    def _notify_dependents(self, changed):
        for dependent in self._dependents:
            dependent._recalculate(changed)


class InputCell(Cell):
    def __init__(self, initial_value):
        super().__init__()
        self._value = initial_value


class ComputeCell(Cell):
    def __init__(self, inputs, compute_function):
        super().__init__()
        self._inputs = inputs
        self._compute_function = compute_function
        self._callbacks = []

        for input_cell in self._inputs:
            input_cell._dependents.append(self)

        self._value = self._compute()

    def _compute(self):
        return self._compute_function([i.value for i in self._inputs])

    def _recalculate(self, changed):
        new_value = self._compute()
        if new_value != self._value:
            changed.setdefault(self, self._value)
            self._value = new_value
            self._notify_dependents(changed)

    def add_callback(self, callback):
        if callback not in self._callbacks:
            self._callbacks.append(callback)

    def remove_callback(self, callback):
        if callback in self._callbacks:
            self._callbacks.remove(callback)

    def _trigger_callbacks(self):
        for cb in self._callbacks:
            cb(self.value)
