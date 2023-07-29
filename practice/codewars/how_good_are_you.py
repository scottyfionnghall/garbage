def better_than_average(class_points, your_points):
    avarage = 0
    for point in class_points:
        avarage += point
    avarage = avarage / len(class_points)
    if your_points > avarage:
        return True
    else:
        return False

better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75)