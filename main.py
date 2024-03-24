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