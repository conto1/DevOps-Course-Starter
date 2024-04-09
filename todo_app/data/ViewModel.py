from todo_app.data.Item import Item

class ViewModel:
    def __init__(self, list_items):
        self._items = list_items
 
    @property
    def items(self):
        return self._items
    
    @property
    def todo_items(self):
        output_list = []

        for item in self.items:
            if item.status == "To do":
                output_list.append(item)
                
        return output_list
    
    @property
    def doing_items(self):
        output_list = []

        for item in self.items:
            if item.status == "Doing":
                output_list.append(item)
                
        return output_list
    
    @property
    def done_items(self):
        output_list = []

        for item in self.items:
            if item.status == "Done":
                output_list.append(item)
                
        return output_list