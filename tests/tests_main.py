from todo_app.viewmodel import ViewModel
from todo_app.data import session_items

# def test_viewmodel():

    #  # Arrange
    # items_in_doing = [{'id': '60aae7e68ae1e01db6226b86', 'status': 'Not Started', 'title': 'Learn JSON'},
    #                   {'id': '60cdfc1746d7211010266ff7', 'status': 'Not Started', 'title': 'Learn XML'}]
    
    # # Act
    # items = session_items.get_items()
    
    # # Assert
    # print(" ")
    # print(" ")
    # print ('items_in_doing:')
    # print(items_in_doing)
    
    # print(" ")
    # print ('items:')
    # print(items)
    
    # assert items_in_doing == items
    
    # item = ['Test ID', 'ToDo', 'A test description']
    # testView = ViewModel(item)

    # print(str.testView)
    
    # pass





# import pytest

def test_upper():
    assert 'foo'.upper() == 'FOO'

def test_isupper():
    assert 'FOO'.isupper()
    assert not 'Foo'.isupper()