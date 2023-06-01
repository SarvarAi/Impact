class Parent1:
    def __init__(self):
        super().__init__()
        print("Parent1's __init__ method called")

class Parent2:
    def __init__(self):
        super().__init__()
        print("Parent2's __init__ method called")

class Child(Parent1, Parent2):
    def __init__(self):
        super().__init__()
        print("Child's __init__ method called")

child = Child()