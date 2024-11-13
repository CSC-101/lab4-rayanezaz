import data
import lab4
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def testFirstElement1(self):
        input = [[3,5], [2,9]]
        result = lab4.first_element(input)
        expected = [3, 2]
        self.assertEqual(expected, result)

    def testFirstElement2(self):
        input = [[0, 3], [], [9, 0]]
        result = lab4.first_element(input)
        expected = [0, 9]
        self.assertEqual(expected, result)

    # Part 2
    def test_x_coordiantes1(self):
        input = [data.Point(5,0),data.Point(3,2),data.Point(7,8),data.Point(0,3)]
        result = lab4.x_coordinates(input)
        expected = [5, 3, 7, 0]
        self.assertEqual(expected, result)
    def test_x_coordinates2(self):
        input = [data.Point(9,1),data.Point(2,7), data.Point(-5,8),data.Point(-1,0)]
        result = lab4.x_coordinates(input)
        expected = [9,2,-5,-1]
        self.assertEqual(expected, result)

    # Part 3
    def testAreInPositiveQuadrant1(self):
        input = [data.Point(4, 0), data.Point(5, -3), data.Point(5, 4), data.Point(-1, -5)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [[5, 4]]
        self.assertEqual(expected, result)

    def testAreInPositiveQuadrant2(self):
        input = [data.Point(5, -9), data.Point(5, 3), data.Point(-1, -1), data.Point(101, 2)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [[5, 3], [101, 2]]
        self.assertEqual(expected, result)

   # Part 4
    def testDistance1(self):
        input1 = data.Point(6, 9)
        input2 = data.Point(3, 5)
        result = lab4.distance(input1, input2)
        expected = 5
        self.assertEqual(expected, result)

    def testDistance2(self):
        input1 = data.Point(9, 9)
        input2 = data.Point(1, 3)
        result = lab4.distance(input1, input2)
        expected = 10
        self.assertEqual(expected, result)

    # Part 5
    def testManhattanDistance1(self):
        input1 = data.Point(5, 3)
        input2 = data.Point(1, 0)
        result = lab4.manhattan_distance(input1, input2)
        expected =  7
        self.assertEqual(expected, result)

    def testManhattanDistance2(self):
        input1 = data.Point(4, 2)
        input2 = data.Point(5,1)
        result = lab4.manhattan_distance(input1, input2)
        expected = 2
        self.assertEqual(expected, result)

    # Part 6
    def testDistanceAll1(self):
        input = [data.Point(12, 9)]
        result = lab4.distance_all(input)
        expected = 15
        self.assertEqual(expected, result)

    def testDistanceAll2(self):
        input = [data.Point(2, 1)]
        result = lab4.distance_all(input)
        expected = 2.24
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()