# Trójkąt
def triangle_area(base, height):
    """
    Calculates the area of a triangle given its base and height.
    
    Args:
    - base (float): The base of the triangle.
    - height (float): The height of the triangle.
    
    Returns:
    - float: The area of the triangle.
    """
    area = 0.5 * base * height
    return area

# Example usage:
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = triangle_area(base, height)
print("The area of the triangle is:", area)

# Kwadrat
def square_area(side_length):
    """
    Calculates the area of a square given the length of its side.
    
    Args:
    - side_length (float): The length of a side of the square.
    
    Returns:
    - float: The area of the square.
    """
    area_sq = side_length * side_length
    return area_sq

# Example usage:
side_length = float(input("Enter the length of a side of the square: "))

area_sq = square_area(side_length)
print("The area of the square is:", area_sq)
