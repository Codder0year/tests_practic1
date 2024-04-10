def color():
    print("Введите 2 цвета: желтый, красный, синий")
    one_color = input("Введите первый цвет: ")
    two_color = input("Введите второй цвет: ")
    valid_colors = ["красный", "синий", "желтый"]
    if one_color not in valid_colors or two_color not in valid_colors:
        return "блаблабла"
    if one_color == "красный":
        if two_color == "синий":
            return "фиолетовый"
        elif two_color == "желтый":
            return "оранжевый"
        elif two_color == "красный":
            return "красный"
    elif one_color == "синий":
        if two_color == "желтый":
            return "зеленый"
        elif two_color == "красный":
            return "фиолетовый"
        elif two_color == "синий":
            return "синий"
    elif one_color == "желтый":
        if two_color == "синий":
            return "зеленый"
        elif two_color == "красный":
            return "оранжевый"
        elif two_color == "желтый":
            return "желтый"

print(color())