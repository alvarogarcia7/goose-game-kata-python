from __future__ import annotations


class Player:
    def __init__(self, name: str, position: int) -> None:
        self.name = name
        self.position = position

    def move(self, spaces):
        self.position += spaces

    def __eq__(self, o: object) -> bool:
        return o.name == self.name and o.position == self.position


class Game:
    def __init__(self, players: PlayerRepository) -> None:
        self.players = players
        self.user_names = []
        self.ui_representation = UIRepresentation()

    def run(self, user_input: str):
        user_input_parts = user_input.split(" ")
        user_name = user_input_parts[-1]
        self.user_names.append(user_name)
        action = user_input_parts[0]
        if action == 'move':
            user_name = user_input_parts[1]
            die_values = list(map(lambda x: x.strip().replace(',', ''), user_input_parts[-2:]))
            sum_of_die = sum(map(lambda x: int(x), die_values))
            user = self.players.find_by_name(user_name)
            previous_position = self.ui_representation.position(user.position)
            user.move(sum_of_die)
            current_position = self.ui_representation.position(user.position)
            return f'{user_name} rolls {", ".join(die_values)}. Pippo moves from {previous_position} to {current_position}'
        try:
            self.players.add(Player(user_name, 0))
        except Exception:
            return f"{user_name}: already existing player"
        names = list(map(lambda player: player.name, self.players.find_all()))
        return f"players: {', '.join(names)}"


class PlayerRepository:
    def __init__(self):
        self.names = []

    def add(self, name: Player):
        if name in self.names:
            raise Exception("Repeated user")

        self.names.append(name)

    def find_all(self) -> [Player]:
        return self.names

    def find_by_name(self, name):
        return list(filter(lambda player: player.name == name, self.names))[0]


class UIRepresentation:
    def position(self, index_of_position) -> str:
        result = str(index_of_position)
        if not index_of_position:
            result = 'Start'
        return result
