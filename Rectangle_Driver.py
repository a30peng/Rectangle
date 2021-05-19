import io
import sys
import unittest
from Rectangle import *

"""
A unit test driver to test the functionality of the rectangle class and helper functions. The unit test should all your 
to run either all of them at the same time or one at a time. This should make isolating certain functionality easier.
"""

class TestStringMethods(unittest.TestCase):
    """
    Unit test to check whether or not two rectangles intersect
    """

    def test_intersection_positive_check(self):
        # Intersection positive check
        Rect1 = Rectangle(4, 4, 8, 8)
        Rect2 = Rectangle(5, 5, 9, 9)
        Rect3 = new_rect(Rect1, Rect2)

        print(f'Rectangle 1: {Rect1.toString()}')
        print(f'Rectangle 2: {Rect2.toString()}')
        print(f'Rectangle 3: {Rect3.toString()}')
        print()

        result = []
        found = False
        if find_intersection(Rect1, Rect2, Rect3) == [(8, 5), (5, 8)]:
            found = True
        result.append(found)
        # Intersection positive check
        Rect1 = Rectangle(3, 4, 8, 6)
        Rect2 = Rectangle(4, 5, 7, 7)
        Rect3 = new_rect(Rect1, Rect2)

        print(f'Rectangle 1: {Rect1.toString()}')
        print(f'Rectangle 2: {Rect2.toString()}')
        print(f'Rectangle 3: {Rect3.toString()}')
        print()

        found = False
        if find_intersection(Rect1, Rect2, Rect3) == [(4, 6), (7, 6)]:
            found = True
        result.append(found)

        # Intersection negative and containment negative check
        # ans: ''
        Rect1 = Rectangle(2, 3, 4, 5)
        Rect2 = Rectangle(5, 2, 7, 3)
        Rect3 = new_rect(Rect1, Rect2)

        print(f'Rectangle 1: {Rect1.toString()}')
        print(f'Rectangle 2: {Rect2.toString()}')
        print(f'Rectangle 3: {Rect3.toString()}')
        print()

        found = False
        if find_intersection(Rect1, Rect2, Rect3) == '':
            found = True

        result.append(found)
        self.assertTrue(all(result))

    """
    Unit test to check whether one rectangle contains another
    """

    def test_containment_positive_check(self):
        # Containment check: positive
        # ans: (3, 3), (4, 4), (3, 4), (4, 3)
        Rect1 = Rectangle(2, 2, 5, 6)
        Rect2 = Rectangle(3, 4, 4, 3)
        Rect3 = new_rect(Rect1, Rect2)

        print(f'Rectangle 1: {Rect1.toString()}')
        print(f'Rectangle 2: {Rect2.toString()}')
        print(f'Rectangle 3: {Rect3.toString()}')
        print()

        result = []
        found = False
        if find_containment(Rect1, Rect2, Rect3) == '(3, 3), (4, 4), (3, 4), (4, 3)':
            found = True
        result.append(found)

        # Intersection negative and containment negative check
        # ans: ''
        Rect1 = Rectangle(2, 3, 4, 5)
        Rect2 = Rectangle(5, 2, 7, 3)
        Rect3 = new_rect(Rect1, Rect2)

        print(f'Rectangle 1: {Rect1.toString()}')
        print(f'Rectangle 2: {Rect2.toString()}')
        print(f'Rectangle 3: {Rect3.toString()}')
        print()

        found = False
        if find_containment(Rect1, Rect2, Rect3) == '':
            found = True

        result.append(found)
        self.assertTrue(all(result))

    """
    Unit test to check whether or not two rectangles have subline adjacency
    """

    def test_subline_adjacency_positive_check(self):
        # Adjacency check top-bottom Subline: positive
        # ans: Subline adjacency detected at points: (4, 6), (5, 6), (4, 6), (5, 6)
        Rect1 = Rectangle(3, 3, 6, 6)
        Rect2 = Rectangle(4, 6, 5, 8)
        Rect3 = new_rect(Rect1, Rect2)

        print(f'Rectangle 1: {Rect1.toString()}')
        print(f'Rectangle 2: {Rect2.toString()}')
        print(f'Rectangle 3: {Rect3.toString()}')
        print()

        result = []
        found = False
        if str(find_adjacency(Rect1, Rect2, Rect3)[0]) == '(4, 6), (5, 6), (4, 6), (5, 6)':
            found = True
        result.append(found)

        # Adjacency check left-right Subline: positive
        # ans: Subline adjacency detected at points: (5, 6), (5, 5), (5, 5), (5, 6)
        Rect1 = Rectangle(2, 4, 5, 7)
        Rect2 = Rectangle(5, 5, 9, 6)
        Rect3 = new_rect(Rect1, Rect2)

        print(f'Rectangle 1: {Rect1.toString()}')
        print(f'Rectangle 2: {Rect2.toString()}')
        print(f'Rectangle 3: {Rect3.toString()}')
        print()

        found = False
        if str(find_adjacency(Rect1, Rect2, Rect3)[0]) == '(5, 6), (5, 5), (5, 5), (5, 6)':
            found = True
        result.append(found)

        self.assertTrue(all(result))

    """
    Unit test to check whether or not two rectangles have proper adjacency
    """

    def test_proper_adjacency_positive_check(self):
        # Adjacency check top-bottom proper: positive
        # Proper adjacency detected at points: (3, 5), (6, 5), (3, 5), (6, 5)
        Rect1 = Rectangle(3, 3, 6, 5)
        Rect2 = Rectangle(3, 5, 6, 8)
        Rect3 = new_rect(Rect1, Rect2)

        print(f'Rectangle 1: {Rect1.toString()}')
        print(f'Rectangle 2: {Rect2.toString()}')
        print(f'Rectangle 3: {Rect3.toString()}')
        print()

        result = []
        found = False
        if str(find_adjacency(Rect1, Rect2, Rect3)[1]) == '(3, 5), (6, 5), (3, 5), (6, 5)':
            found = True
        result.append(found)
        self.assertTrue(all(result))

    """
    Unit test to check whether or not two rectangles have partial adjacency
    """

    def test_partial_adjacency_positive_check(self):
        # Adjacency check top-bottom partial: positive
        # Partial adjacency detected at points: (6, 6), (6, 4), (6, 4), (6, 6)
        Rect1 = Rectangle(3, 3, 6, 6)
        Rect2 = Rectangle(6, 4, 9, 8)
        Rect3 = new_rect(Rect1, Rect2)

        print(f'Rectangle 1: {Rect1.toString()}')
        print(f'Rectangle 2: {Rect2.toString()}')
        print(f'Rectangle 3: {Rect3.toString()}')
        print()

        result = []
        found = False
        if str(find_adjacency(Rect1, Rect2, Rect3)[2]) == '(6, 6), (6, 4), (6, 4), (6, 6)':
            found = True
        result.append(found)

        self.assertTrue(all(result))


if __name__ == '__main__':
    unittest.main()
