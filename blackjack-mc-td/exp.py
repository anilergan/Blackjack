class Parent:
    def __init__(self):
        print('Parent is initialized.')
        self.parent_attr = 10
        
    
    def change_parent_attr(self):
        self.parent_attr = 99
        

    def display_parent_attr(self):
        print('Parent attr:', self.parent_attr)

    def craete_sub_class_object(self):
        sub_class_obj = Child()
        sub_class_obj.call_super_class_object()
        


class Child(Parent):
    def __init__(self):
        print('Child is initialized.')
        super().__init__()
        print('Childs super is initialized.')

    def call_super_class_object(self):
        print('Child method is called')
        self.change_parent_attr()
        self.display_parent_attr()
    
    

parent_obj = Parent()
parent_obj.craete_sub_class_object()




