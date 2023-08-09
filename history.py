class History:
    def __init__(self):
        self.history = []

    def add_to_history(self, name, response):
        self.history.append(f"{name} says: {response}")

    def get_full_history(self):
        return "\n".join(self.history)