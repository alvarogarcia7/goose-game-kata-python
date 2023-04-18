import unittest

from tests.main import Game, PlayerRepository
from unittest.mock import Mock, MagicMock


class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.players = PlayerRepository()
        self.players.find_all = MagicMock(return_value=[])
        self.game = Game(self.players)

    def test_add_a_player(self):
        self.players.add = MagicMock()

        self.game.run("add player Pippo")

        self.players.add.assert_called_with('Pippo')

    def test_formatting_of_the_resulting_players(self):
        self.players.find_all = MagicMock(return_value=['Pippo', 'Pluto'])

        response = self.game.run("")

        self.assertEquals(response, "players: Pippo, Pluto")

    def test_when_there_is_an_exception_when_adding_a_player(self):
        self.players.add = Mock(side_effect=Exception())

        response = self.game.run("add player Pippo")

        self.assertEquals(response, "Pippo: already existing player")


class TestPlayers(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.players = PlayerRepository()

    def test_add_a_player(self):
        self.players.add('player_name')

        self.assertEquals(self.players.find_all(), ['player_name'])

    def test_add_a_second_player(self):
        self.players.add('player_name_1')

        self.players.add('player_name_2')

        self.assertEquals(self.players.find_all(), ['player_name_1', 'player_name_2'])

    def test_cannot_add_a_repeated_player(self):
        self.players.add("Pippo")

        with self.assertRaises(Exception):
            self.players.add("Pippo")
