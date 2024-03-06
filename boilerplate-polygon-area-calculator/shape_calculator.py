class Rectangle:
    # INITIALIZE THE WIDTH AND HEIGHT OF OBJECT (RECTANGLE)
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # RETURNS STRING IF OBJECT (RECTANGLE) IS PRINTED ON STR
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    # RETURNS STRING IF OBJECT (RECTANGLE) IS PRINTED IN THE REPL
    def __repl__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    # SETS THE WIDTH OF THE OBJECT (RECTANGLE)
    def set_width(self, width):
        self.width = width

    # SETS THE HEIGHT OF THE OBJECT (RECTANGLE)
    def set_height(self, height):
        self.height = height

    # RETURNS THE AREA OF THE OBJECT (RECTANGLE)
    def get_area(self):
        return self.width * self.height

    # RETURNS THE PERIMETER OF THE OBJECT (RECTANGLE)
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    # RETURNS THE DIAGONAL OF THE OBJECT (RECTANGLE)
    def get_diagonal(self):
        return ((self.width**2) + (self.height**2)) ** 0.5

    # IF HIGHER THAN 50 (WIDTH OR HEIGHT) RETURNS AN ERROR MESSAGE, UNLESS IT PRINTS OUT THE SHAPE WITH '*' CHARACTER
    def get_picture(self):
        if (self.width > 50) or (self.height > 50):
            return "Too big for picture."
        else:
            picture = ""

            for row in range(self.height):
                for column in range(self.width):
                    picture += "*"
                picture += "\n"

            return picture

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)


class Square(Rectangle):
    # INITIALIZE THE SIDE OF OBJECT (SQUARE) AND MODIFIES __INIT__ METHOD TO HAVE ONLY 1 PARAMETER (SIDE)
    def __init__(self, side):
        super().__init__(side, side)

    # RETURNS STRING IF OBJECT (SQUARE) IS PRINTED ON STR
    def __str__(self):
        return f"Square(side={self.width})"

    # RETURNS STRING IF OBJECT (SQUARE) IS PRINTED IN THE REPL
    def __repl__(self):
        return f"Square(side={self.width})"

    # SETS THE WIDTH AND THE HEIGHT OF THE OBJECT (SQUARE)
    def set_side(self, side):
        self.width = side
        self.height = side

    # SETS THE WIDTH AND THE HEIGHT OF THE OBJECT (SQUARE)
    def set_width(self, side):
        self.width = side
        self.height = side

    # SETS THE WIDTH AND THE HEIGHT OF THE OBJECT (SQUARE)
    def set_height(self, side):
        self.width = side
        self.height = side
