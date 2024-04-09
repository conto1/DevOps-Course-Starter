from todo_app.data.Item import Item
from todo_app.data.ViewModel import ViewModel  


def test_view_model_items_not_started():
    
    #Arrange
    items = [ 
        Item("1", "to do item","To do"),
        Item("2", "in progress items", "Doing"),
        Item("3", "completed items", "Done")
    ]
    view_model = ViewModel(items)
    print(view_model)
    #Act
    returned_items = view_model.todo_items
    print(returned_items)
    #Assert 
    assert len(returned_items) == 1
    single_item = returned_items[0]
    assert single_item.status == "To do"
