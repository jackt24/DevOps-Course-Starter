from todo_app import viewmodel
from todo_app.viewmodel import ViewModel
from todo_app.data import session_items
from todo_app.item import Item


def test_ToDoItems():
    items = [
        Item('Task 1', "ToDo",'hello'),
        Item('Task 2', "Complete", 'hello'),
        Item('Task 3', "Doing", 'hello')
    ]

    view_model = ViewModel(items)

    assert len(view_model.to_do_items) == 1

def test_CompletedItems():
    items = [
        Item('Task 1', "ToDo",'hello'),
        Item('Task 2', "Complete", 'hello'),
        Item('Task 3', "Doing", 'hello')
    ]
    
    view_model = ViewModel(items)

    assert len(view_model.complete_items) == 1

def test_DoingItems():
    items = [
        Item('Task 1', "ToDo",'hello'),
        Item('Task 2', "Complete", 'hello'),
        Item('Task 3', "Doing", 'hello')
    ]
    
    view_model = ViewModel(items)

    assert len(view_model.doing_items) == 1

