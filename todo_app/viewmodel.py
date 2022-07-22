# Class that collates template information
class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def to_do_items(self):
        return [item for item in self._items if item.status == 'ToDo']

    # Not Currently in Use 
    # @property
    # def doing_items(self):
    #     return [item for item in self._items if item.status == 'Doing']

    @property
    def complete_items(self):
        return [item for item in self._items if item.status == 'Complete']