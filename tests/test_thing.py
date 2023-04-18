import unittest

from app.thing import Thing


class Game:
    def __init__(self) -> None:
        self.user_names = []

    def run(self, user_input: str):
        self.user_names.append(user_input.split(" ")[-1])
        return f"players: {', '.join(self.user_names)}"


class TestThing(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.game = Game()

    def test_add_first_player(self):
        response = self.game.run("add player Pippo")

        self.assertEquals(response, "players: Pippo")

    def test_add_second_player(self):
        self.game.run("add player Pippo")

        response = self.game.run("add player Pluto")

        self.assertEquals(response, "players: Pippo, Pluto")
