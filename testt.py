import math

def logarifm(f: float, g: float, h: float) -> float:

    if f <= 0:
        raise ValueError("аргумент логарифма f должен быть строго больше 0")
    if h == 1:
        raise ValueError("параметр h не должен быть равен 1")
        
    return math.log(f) + g / (h - 1)



    