import unittest
from game_of_life.logic import GameMatrix
from game_of_life.gui import App

class GameMatrixTestCase(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.matrix = self.app.game_grid.matrix

    def test_neighbours(self):
        for key, cell in enumerate(((1,1), (6,3), (4,4))):
            with self.subTest(key):
                shift_i = cell[0] - 1
                shift_j = cell[1] - 1
                self.assertEqual(
                    self.matrix.neighbours(cell),
                    {(i, j) for i in range(shift_i, shift_i + 3) 
                    for j in range(shift_j, shift_j + 3) 
                    if i != cell[0] or j != cell[1]})

    def test_alive_neighbours(self):
        color1, color2 = self.app.ALIVE_COLORS
        with self.subTest(0):
            self.matrix._alive = {
                (0, 0): color1, (0, 1): color1, (1, 0): color2,
                (0, 2): color1, (5, 1): color1, (2, 3): color2,}
            self.assertEqual(
                self.matrix.alive_neighbours((1,1)),
                {(0, 0), (0, 1), (1, 0), (0, 2)}
            )
        with self.subTest(1):
            self.matrix._alive = {
                (i, j): color1 
                for i in range(3)
                for j in range(3)}
            self.assertEqual(
                self.matrix.alive_neighbours((1, 1)), 
                {(i, j) for j in range(3) for i in range(3) 
                if i != 1 or j != 1})
        with self.subTest(2):
            self.matrix._alive = {
                (0, 8): color1, (1, 1): color1, (5, 1): color1}
            self.assertEqual(
                self.matrix.alive_neighbours((1, 1)), set())
    
    def test_dead_neighbours(self):
        color1, color2 = self.app.ALIVE_COLORS
        with self.subTest(0):
            self.matrix._alive = {
                (0, 0): color1, (0, 1): color1, (1, 0): color2,
                (0, 2): color1, (5, 1): color1, (2, 3): color2}
            self.assertEqual(
                self.matrix.dead_neighbours((1, 1)),
                {(1, 2), (2, 0), (2, 1), (2, 2)})
        with self.subTest(1):
            self.matrix._alive = {
                (i, j): color1 
                for i in range(3)
                for j in range(3)}
            self.assertEqual(
                self.matrix.dead_neighbours((1, 1)), set())
        with self.subTest(2):
            self.matrix._alive = {
                (0, 8): color1, (1, 1): color1, (5, 1): color1}
            self.assertEqual(
                self.matrix.dead_neighbours((1, 1)),
                {(i, j) for j in range(3) for i in range(3) 
                if i != 1 or j != 1})

    def test_alive(self):
        color1, color2 = self.app.ALIVE_COLORS
        with self.subTest(0):
            alive = self.matrix.alive
            self.assertIsNot(alive, self.matrix._alive)
        with self.subTest(1):
            self.matrix._alive = {
                (0, 0): color1, (0, 2): color1, (0, 3): color2}
            alive = self.matrix.alive
            self.assertIsNot(alive, self.matrix._alive)

    def test_make_step(self):
        color1, color2 = self.app.ALIVE_COLORS
        with self.subTest(0):
            self.matrix._alive = {
                (0, 0): color1, (0, 2): color1, (0, 3): color2}
            self.matrix.make_step()
            self.assertEqual(
                self.matrix.alive, {})
        with self.subTest(1):
            self.matrix._alive = {
                (0, 0): color1, (0, 1): color1, (1, 0): color2}
            self.matrix.make_step()
            self.assertEqual(
                self.matrix.alive,
                {(0, 0): color1, (0, 1): color1, 
                (1, 0): color2, (1, 1): color1})
        with self.subTest(2):
            dict_red = {(i, i): color1 for i in range(5,9)}
            dict_blue = {(i, 13 - i): color2 for i in range(5,9)}
            dict_red.update(dict_blue)
            self.matrix._alive = dict_red
            self.matrix.make_step()
            self.assertEqual(
                self.matrix.alive,
                {(5, 6): color1, (6, 5): color1, 
                (7, 8): color1, (8, 7): color1,
                (7, 5): color2, (8, 6): color2, 
                (5, 7): color2, (6, 8): color2})


if __name__ == '__main__':
    unittest.main()