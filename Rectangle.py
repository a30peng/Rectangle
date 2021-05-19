"""
A class that given two points (x1,y1),(x2,y2) will generate a rectangle with all four points
"""


class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        self.bottom_left = (x1, y1)
        self.top_right = (x2, y2)
        self.bottom_right = (x2, y1)
        self.top_left = (x1, y2)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.tuple_list = [self.bottom_left, self.top_right, self.bottom_right, self.top_left]

    """
    A function that will return the two given points of the rectangle as a formatted string
    
    :return: Formatted string
    """

    def toString(self):
        to_string = f'({self.x1}, {self.y1}), ({self.x2}, {self.y2})'
        return to_string

    """
    A function that will return all four points of your rectangle as a formatted string
    
    :return: Formatted string
    """

    def rect_points(self):
        to_string = f'({self.x1}, {self.y2}), ({self.x2}, {self.y1}), ({self.x1}, {self.y1}), ({self.x2}, {self.y2})'
        return to_string


"""A function that given two rectangles will return a third encompassed rectangle, that is used to find things such 
as intersection points, containtment and adjacency 

:param p1: Rectangle r1 
:param p2: Rectangle r2 
:return: Rectangle 
"""


def new_rect(r1, r2):
    x5 = max(r1.x1, r2.x1)
    y5 = max(r1.y1, r2.y1)
    x6 = min(r1.x2, r2.x2)
    y6 = min(r1.y2, r2.y2)

    return Rectangle(x5, y5, x6, y6)


"""
A function that given three rectangles will find all the unique values in r3 compared against r1, r2. 

:param p1: Rectangle r1
:param p2: Rectangle r2
:param p3: Rectangle r3
:return: List of unique values in r3
"""


def tuple_exists(r1, r2, r3):
    r1_list = r1.tuple_list
    r2_list = r2.tuple_list
    r3_list = r3.tuple_list
    r3_list = list(set(r3_list) - set(r2_list))

    r3_list = list(set(r3_list) - set(r1_list))

    return r3_list


"""
A function that given three rectangles will find the intersection points, R3, and return the result. 

:param p1: Rectangle r1
:param p2: Rectangle r2
:param p3: Rectangle r3
:return: List of the intersecting points or empty string ''.
"""


def find_intersection(r1, r2, r3):
    intersection = ''
    if (r3.x1 < r3.x2) and (r3.y1 < r3.y2):
        print(f'Found intersection at points {r3.rect_points()}')
        print(f'Intersection {tuple_exists(r1, r2, r3)}')
        intersection = tuple_exists(r1, r2, r3)
    else:
        print(f'Intersection not found for points {r3.rect_points()}')

    return intersection


"""A function that given three rectangles will find whether the rectangles R1, R2 have subline adjacency, 
proper_adjacency or partial_adjacency. 

:param p1: Rectangle r1 
:param p2: Rectangle r2 
:param p3: Rectangle r3 
:return: List of points where adjacency 
occur. Where position [0] is the subline adjacency point, [1] is the proper adjacency point and [2] is the partial 
adjacency point. If no adjacency is found and empty string replaces the value in the list. (e.g ['','',''])
"""


def find_adjacency(r1, r2, r3):
    found = []
    # top-bottom adjacency
    print(f'Looking for adjacency')
    if (r3.bottom_left == r3.top_left) and (r3.bottom_right == r3.top_right):
        found.append(check_subline_adjacency_top_bottom(r1, r2, r3))
        found.append(check_proper_adjacency_top_bottom(r1, r2, r3))
        found.append(check_partial_adjacency_top_bottom(r1, r2, r3))

    # left-right adjacency
    elif (r3.bottom_left == r3.bottom_right) and (r3.top_right == r3.top_right):
        found.append(check_subline_adjacency_left_right(r1, r2, r3))
        found.append(check_proper_adjacency_left_right(r1, r2, r3))
        found.append(check_partial_adjacency_left_right(r1, r2, r3))

    if not any(found):
        print(f'Adjacency not found')
    return found


"""A function that given three rectangles will find whether the rectangles R1, R2 have subline adjacency for the top 
and bottom sides of the rectangles.

:param p1: Rectangle r1 
:param p2: Rectangle r2 
:param p3: Rectangle r3 
:return: Set of points where adjacency occurs or empty string ''. (e.g (6, 6), (6, 4), (6, 4), (6, 6))
"""


def check_subline_adjacency_top_bottom(r1, r2, r3):
    found = ''
    if ((r2.x1 > r1.x1) and (r2.x2 < r1.x2)) or ((r2.x1 < r1.x1) and (r2.x2 > r1.x2)):
        print(f'Subline adjacency detected at points: {r3.rect_points()}')
        found = r3.rect_points()
    return found


"""A function that given three rectangles will find whether the rectangles R1, R2 have subline adjacency for the left 
and right sides of the rectangles.

:param p1: Rectangle r1 
:param p2: Rectangle r2 
:param p3: Rectangle r3 
:return: Set of points where adjacency occurs or empty string ''. (e.g (6, 6), (6, 4), (6, 4), (6, 6))
"""


def check_subline_adjacency_left_right(r1, r2, r3):
    found = ''
    if ((r2.y1 > r1.y1) and (r2.y2 < r1.y2)) or ((r2.y1 < r1.y1) and (r2.y2 > r1.y2)):
        print(f'Subline adjacency detected at points: {r3.rect_points()}')
        found = r3.rect_points()
    return found


"""A function that given three rectangles will find whether the rectangles R1, R2 have proper adjacency for the top 
and bottom sides of the rectangles.

:param p1: Rectangle r1 
:param p2: Rectangle r2 
:param p3: Rectangle r3 
:return: Set of points where adjacency occurs or empty string ''. (e.g (6, 6), (6, 4), (6, 4), (6, 6))
"""


def check_proper_adjacency_top_bottom(r1, r2, r3):
    found = ''
    if ((r2.x1 == r1.x1) and (r2.x2 == r1.x2)) or ((r2.x1 == r1.x1) and (r2.x2 == r1.x2)):
        print(f'Proper adjacency detected at points: {r3.rect_points()}')
        found = r3.rect_points()
    return found


"""A function that given three rectangles will find whether the rectangles R1, R2 have proper adjacency for the left 
and right sides of the rectangles.

:param p1: Rectangle r1 
:param p2: Rectangle r2 
:param p3: Rectangle r3 
:return: Set of points where adjacency occurs or empty string ''. (e.g (6, 6), (6, 4), (6, 4), (6, 6))
"""


def check_proper_adjacency_left_right(r1, r2, r3):
    found = ''
    if ((r2.y1 == r1.y1) and (r2.y2 == r1.y2)) or ((r2.y1 == r1.y1) and (r2.y2 == r1.y2)):
        print(f'Proper adjacency detected at points: {r3.rect_points()}')
        found = r3.rect_points()
    return found


"""A function that given three rectangles will find whether the rectangles R1, R2 have partial adjacency for the top 
and bottom sides of the rectangles.

:param p1: Rectangle r1 
:param p2: Rectangle r2 
:param p3: Rectangle r3 
:return: Set of points where adjacency occurs or empty string ''. (e.g (6, 6), (6, 4), (6, 4), (6, 6))
"""


def check_partial_adjacency_left_right(r1, r2, r3):
    found = ''
    if ((r2.y2 > r1.y2) and (r1.y2 > r2.y1) and (r2.y2 > r1.y1)) or (
            (r2.y2 < r1.y2) and (r1.y2 < r2.y1) and (r2.y2 < r1.y1)):
        print(f'Partial adjacency detected at points: {r3.rect_points()}')
        found = r3.rect_points()
    return found


"""A function that given three rectangles will find whether the rectangles R1, R2 have partial adjacency for the left 
and right sides of the rectangles.

:param p1: Rectangle r1 
:param p2: Rectangle r2 
:param p3: Rectangle r3 
:return: Set of points where adjacency occurs or empty string ''. (e.g (6, 6), (6, 4), (6, 4), (6, 6))
"""


def check_partial_adjacency_top_bottom(r1, r2, r3):
    found = ''
    if ((r2.x2 > r1.x2) and (r1.x2 > r2.x1) and (r2.x2 > r1.x1)) or (
            (r2.x2 < r1.x2) and (r1.x2 < r2.x1) and (r2.x2 < r1.x1)):
        print(f'Partial adjacency detected at points: {r3.rect_points()}')
        found = r3.rect_points()
    return found


"""A function that given three rectangles will find whether the rectangle r1 is contained within rectangle r2 
or if r2 is contained in rectangle r1. The contained rectangle is defined as r3 the result of r1,r2. r3 should equal 
either r1 or r2 is there is containment.

:param p1: Rectangle r1 
:param p2: Rectangle r2 
:param p3: Rectangle r3 
:return: Set of points where containment occurs. (e.g (6, 6), (6, 4), (6, 4), (6, 6))
"""


def find_containment(r1, r2, r3):
    found = ''
    if rect_found(r3, r1) or rect_found(r3, r2):
        found = r3.rect_points()
        print(f'Found containment at points {r3.rect_points()}')
    else:
        print(f'Containment not found at points {r3.rect_points()}')

    return found


"""A function that given two rectangles will find whether the rectangle r1 is equal to r2 by comparing the points of r1, 
r2 and creating a boolean list of all points that are equal.

:param p1: Rectangle r1 
:param p2: Rectangle r2 
:param p3: Rectangle r3 
:return: boolean value denoting whether or not the two rectangles have the same points. All point must be equal to 
return true.
"""


def rect_found(r1, r2):
    result = [r1.x1 == r2.x1, r1.y1 == r2.y1, r1.x2 == r2.x2, r1.y2 == r2.y2]

    return all(result)
