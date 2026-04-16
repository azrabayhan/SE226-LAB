import geometry_utils

print("Available shapes: circle, rectangle, triangle")
print("Available calculations: _area, _perimeter (e.g., circle_area)")

operation = input("Enter the operation you want to perform: ")

shape_functions = {
    "circle_area": geometry_utils.circle_area,
    "circle_perimeter": geometry_utils.circle_perimeter,
    "rectangle_area": geometry_utils.rectangle_area,
    "rectangle_perimeter": geometry_utils.rectangle_perimeter,
    "triangle_area": geometry_utils.triangle_area
}

if operation in shape_functions:

    if operation == "circle_area" or operation == "circle_perimeter":
        r = float(input("Enter radius: "))
        result = shape_functions[operation](r)

    elif operation == "rectangle_area" or operation == "rectangle_perimeter":
        w = float(input("Enter width: "))
        h = float(input("Enter height: "))
        result = shape_functions[operation](w, h)

    elif operation == "triangle_area":
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        result = shape_functions[operation](b, h)

    print("Result:", result)

else:
    print("Invalid operation")