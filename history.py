class History:
    def __init__(self):
        self.history = []

    def add_to_history(self, name, response) -> "History":
        self.history.append(f"{name}: {response}")
        return self

    def get_full_history(self) -> str:
        return "\n".join(self.history)