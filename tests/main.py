class Game:
    def __init__(self) -> None:
        self.user_names = []

    def run(self, user_input: str):
        user_name = user_input.split(" ")[-1]
        if user_name in self.user_names:
            return f"{user_name}: already existing player"
        self.user_names.append(user_name)
        return f"players: {', '.join(self.user_names)}"
