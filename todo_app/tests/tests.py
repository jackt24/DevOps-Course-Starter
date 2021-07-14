from todo_app.viewmodel import ViewModel
from flask import pytest

def test_viewmodel():
    
    item = ['Test ID', 'ToDo', 'A test description']
    testView = ViewModel(item)

    print(str.testView)
    
    pass