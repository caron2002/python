def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(radius):
    area = 3.14 * radius * radius
    return area


result1 = get_radius('넓이를 구하고자 하는 원의 반지름은? ')
result2 = get_circle_area(result1)
print(f"반지름 {result1}인 원의 넓이 = 3.14 x {result1} x {result1} = {result2}")
