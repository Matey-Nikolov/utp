import math

def radians_to_gradians (radians):
    gradians_per_radian = 400 / 2
    gradians = radians * (1 / math.pi) * gradians_per_radian

    return  round(gradians, 5)

print(radians_to_gradians(19))