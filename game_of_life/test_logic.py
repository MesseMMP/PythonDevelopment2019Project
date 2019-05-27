import unittest
from game_of_life.logic import GameMatrix
from game_of_life.gui import App

class GameMatrixTestCase(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.matrix = self.app.game_grid.matrix

    def test_neighbours(self):
        self.assertEqual(
            self.matrix.neighbours((1, 1)),
            {(i, j) for j in range(3) for i in range(3) if i != 1 or j != 1}
        )

    def test_alive_neighbours(self):
        color1, color2 = self.app.ALIVE_COLORS
        self.matrix._alive = {
            (0, 0): color1, (0, 1): color1, (1, 0): color2,
            (0, 2): color1, (5, 1): color1, (2, 3): color2,}
        self.assertEqual(
            self.matrix.alive_neighbours((1,1)),
            {(0, 0), (0, 1), (1, 0), (0, 2)}
        )
    
    def test_dead_neighbours(self):
        color1, color2 = self.app.ALIVE_COLORS
        self.matrix._alive = {
            (0, 0): color1, (0, 1): color1, (1, 0): color2,
            (0, 2): color1, (5, 1): color1, (2, 3): color2,}
        self.assertEqual(
            self.matrix.dead_neighbours((1,1)),
            {(1, 2), (2, 0), (2, 1), (2, 2)}
        )

    def test_make_step(self):
        color1, color2 = self.app.ALIVE_COLORS
        self.matrix._alive = {
            (0, 0): color1, (0, 1): color1, (1, 0): color2}
        self.matrix.make_step()
        self.assertEqual(
            self.matrix.alive,
            {(0, 0): color1, (0, 1): color1, (1, 0): color2, (1, 1): color1})


if __name__ == '__main__':
    unittest.main()