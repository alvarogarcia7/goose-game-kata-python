import unittest

from app.thing import Thing


class Game:
    def run(self, user_input: str):
        return "players: Pippo"

class TestThing(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.game = Game()

    def test_add_player(self):

        response = self.game.run("add player Pippo")

        self.assertEquals(response, "players: Pippo")

