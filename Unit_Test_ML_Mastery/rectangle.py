class Rectangle:
    def __init__(self, width, height):
        if width <= 0:
            myError = ValueError('width should be a positive number')
            raise myError
        if height <= 0:
            myError = ValueError("height should be a positive number")
            raise myError
        self.__width = width
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, val):
        self.__height = val
    @property
    def width(self):
        return self.__width
    @width.setter
    def width (self, val):
        self.__width = val

rect = Rectangle(12, 6)
print(f"Width of rectangle: {rect.width}")
print(f"Height of rectangle: {rect.height}")
print(f"Area of Rectangle: {rect.get_area()}")