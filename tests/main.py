class Game:
    def __init__(self) -> None:
        self.user_names = []

    def run(self, user_input: str):
        self.user_names.append(user_input.split(" ")[-1])
        return f"players: {', '.join(self.user_names)}"
