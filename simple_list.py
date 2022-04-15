class SimpleList:
    def __init__(self, items):
        self._items = items

    def add(self, other):
        self._items.append(other)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f'{type(self).__name__}({self._items!r})'


class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(self, items)
        self.sort()

    def add(self, other):
        super.add(self, other)
        self.sort()


class IntList(SimpleList):

    def __init__(self, items=()):
        for x in items: self._validate(x)
        super().__init__(self, items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError('IntList only supports Integer values.')

    def add(self, item):
        self._validate(item)
        super().add(item)


class SortedIntList(IntList, SortedList):
    pass
