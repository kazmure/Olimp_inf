class Point: #Точка #4 Проект не готовий повністю але частково.
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Line: #Лінія
    def __init__(self, p1=Point(), p2=Point()):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"{self.p1} - {self.p2}"


class Circle: #Круг
    def __init__(self, center=Point(), radius=0):
        self.center = center
        self.radius = radius

    def __str__(self):
        return f"Круг з центром {self.center} та радіусом {self.radius}"


class Rectangle: #Прямокутник
    def __init__(self, p1=Point(), p2=Point()):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"Прямокутник з кутами ({self.p1}, {self.p2})"

    #Скоріше за все не вірно працює. Часу не вистачило зробити його нормально.

    # def area(self):
    #     return abs((self.p2.x - self.p1.x) * (self.p2.y - self.p1.y))
    #
    # def perimeter(self):
    #     return 2 * abs((self.p2.x - self.p1.x) + (self.p2.y - self.p1.y))


def main(): #Меню
    print("Оберіть яку хочете фігуру:")
    print("1. Точка")
    print("2. Лінія")
    print("3. Круг")
    print("4. Прямокутник")
    print("5. Вихід")

    while True:
        choice = int(input("Оберіть: "))

        if choice == 1:
            x = int(input("Введіть кординату (x): "))
            y = int(input("Введіть кординату (y): "))
            p = Point(x, y)
            print(f"Точка створена: {p}")

        elif choice == 2:
            x1 = int(input("Введіть кординату (x) для точки 1: "))
            y1 = int(input("Введіть кординату (y) для точки 1: "))
            x2 = int(input("Введіть кординату (x) для точки 2: "))
            y2 = int(input("Введіть кординату (y) для точки 2: "))
            l = Line(Point(x1, y1), Point(x2, y2))
            print(f"Лінія створена: {l}")

        elif choice == 3:
            x = int(input("Введіть кординату (x) для центра"))
            y = int(input("Введіть кординату (x) для центра"))
            r = int(input("Радіус: "))
            c = Circle(Point(x, y), r)
            print(f"Круг створено: {c}")

        elif choice == 4:
            x1 = int(input("Введіть кординату (x) для кута 1: "))
            y1 = int(input("Введіть кординату (y) для кута 1: "))
            x2 = int(input("Введіть кординату (x) для кута 2: "))
            y2 = int(input("Введіть кординату (y) для кута 2: "))
            r = Rectangle(Point(x1, y1), Point(x2, y2))
            print(f"Прямокутник створено: {r}")

        elif choice == 5:
            break

        else:
            print("Помилковий вибір. Заново.")

    print("Вихід з П")


if __name__ == '__main__':
    main()