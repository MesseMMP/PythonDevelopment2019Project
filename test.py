import unittest
import logic as lg

class TestMyMethods(unittest.TestCase):

  def test_one_step_matrix(self):
      self.assertEqual(lg.one_step_matrix([[0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 1, 0], [0, 0, 0, 0]]), [[0, 0, 1, 0], [0, 1, 1, 1], [0, 1, 1, 1], [0, 0, 0, 0]])


  def test_one_step_life_dead(self):
      self.assertEqual(lg.one_step_life_dead([[0,0,0,0],[0,1,1,1],[0,0,1,0],[0,0,0,0]]), ([(0, 2), (2, 1), (2, 3)], [], [[0, 0, 1, 0], [0, 1, 1, 1], [0, 1, 1, 1], [0, 0, 0, 0]]))


if __name__ == '__main__':
    unittest.main()
