# Making your Object Callable:

class Callable:
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print(f"Hello from {self.name}!")


calling = Callable("Harry")
calling()
