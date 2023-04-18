from __future__ import annotations


class Player:
    def __init__(self, name: str, position: int) -> None:
        self.name = name
        self.position = position

    def move(self, spaces: int) -> None:
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
            die_values = self.ui_representation.get_die_values(user_input_parts[-2:])
            sum_of_die = sum(map(lambda x: int(x), die_values))
            user = self.players.find_by_name(user_name)
            previous_position = self.ui_representation.position(user.position)
            user.move(sum_of_die)
            current_position = self.ui_representation.position(user.position)
            moving_message = f'{user_name} rolls {", ".join(die_values)}. {user_name} moves from {previous_position} to {current_position}'
            if user.position == 63:
                moving_message += f". {user_name} wins!!"
            elif user.position > 63:
                current_position = self.ui_representation.position(63)
                moving_message = f'{user_name} rolls {", ".join(die_values)}. {user_name} moves from {previous_position} to {current_position}'
                user.move(2 * (63 - user.position))
                moving_message += f". {user_name} bounces! {user_name} returns to {self.ui_representation.position(user.position)}"
            return moving_message
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

    @staticmethod
    def get_die_values(raw_values: [str]) -> [int]:
        return list(map(lambda x: x.strip().replace(',', ''), raw_values))
