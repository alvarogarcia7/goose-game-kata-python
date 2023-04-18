import unittest

from tests.main import Game


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
