"""
Interface Segragation Principle: clients/subclasses should not be forced
to depend on innterfaces they don't use.
"""

class Shape:
    def draw(self):
        raise NotImplementedError

    def draw_circle(self):
        raise NotImplementedError

    def draw_square(self):
        raise NotImplementedError

    def draw_rectangle(self):
        raise NotImplementedError


"""
Classes Circle and Square implement methods that they don't need.
i.e.
Circle: doesn't need draw_square or draw_rectangle
Square: doesn't need draw_circle
"""
class Circle(Shape):
    def draw_circle(self):
        pass

    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass


class Square(Shape):
    def draw_circle(self):
        pass

    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass


# ideal way
class IShape:
    def draw(self):
        return NotImplementedError


class Circle1(IShape):
    def draw(self):
        # implement draw in a way specific to a circle
        pass


class Square1(IShape):
    def draw(self):
        # implement draw in a way specific to a square
        pass
