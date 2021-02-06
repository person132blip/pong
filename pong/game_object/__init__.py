class GameObject:
    def __init__(self, root):
        self.root = root
        self.window = root.window

    def update(self):
        raise NotImplementedError
    
    def draw(self):
        raise NotImplementedErrors

    def interact(self):
        pass
