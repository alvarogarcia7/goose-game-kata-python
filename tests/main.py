class Game:
    def __init__(self, players) -> None:
        self.players = players
        self.user_names = []

    def run(self, user_input: str):
        user_name = user_input.split(" ")[-1]
        self.user_names.append(user_name)
        try:
            self.players.add(user_name)
        except Exception:
            return f"{user_name}: already existing player"
        return f"players: {', '.join(self.players.find_all())}"


class PlayerRepository:
    def __init__(self):
        self.names = []

    def add(self, name: str):
        if name in self.names:
            raise Exception("Repeated user")

        self.names.append(name)

    def find_all(self) -> [str]:
        return self.names
