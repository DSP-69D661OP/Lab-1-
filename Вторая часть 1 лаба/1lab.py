from typing import Union


class Glass:
    from typing import Union

    class Glass:
        def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
            # Проверка типов
            if not isinstance(capacity_volume, (int, float)):
                raise TypeError("capacity_volume must be an int or a float")
            if not isinstance(occupied_volume, (int, float)):
                raise TypeError("occupied_volume must be an int or a float")

            # Проверка значений
            if capacity_volume <= 0:
                raise ValueError("capacity_volume must be greater than 0")
            if occupied_volume < 0:
                raise ValueError("occupied_volume must be non-negative")
            if occupied_volume > capacity_volume:
                raise ValueError("occupied_volume cannot exceed capacity_volume")

            # Инициализация атрибутов
            self.capacity_volume = capacity_volume
            self.occupied_volume = occupied_volume

        def __repr__(self):
            return f"Glass(capacity_volume={self.capacity_volume}, occupied_volume={self.occupied_volume})"

    if __name__ == "__main__":
        # Корректные объекты
        try:
            glass1 = Glass(500, 300)  # Стакан объемом 500 мл, заполнен на 300 мл
            glass2 = Glass(250, 0)  # Стакан объемом 250 мл, пустой
            print(glass1)
            print(glass2)
        except (TypeError, ValueError) as e:
            print(f"Error while creating a valid Glass object: {e}")

        # Некорректные объекты
        try:
            glass_invalid1 = Glass("500", 300)  # Некорректный тип capacity_volume
        except (TypeError, ValueError) as e:
            print(f"Error: {e}")

        try:
            glass_invalid2 = Glass(500, -100)  # Отрицательный объем
        except (TypeError, ValueError) as e:
            print(f"Error: {e}")

        try:
            glass_invalid3 = Glass(500, 600)  # Заполнено больше, чем вместимость
        except (TypeError, ValueError) as e:
            print(f"Error: {e}")

        try:
            glass_invalid4 = Glass(0, 100)  # Нулевая вместимость
        except (TypeError, ValueError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    try:
        glass1 = Glass(500, 300)  # Стакан объемом 500 мл, заполнен на 300 мл
        glass2 = Glass(250, 0)  # Стакан объемом 250 мл, пустой
        print(glass1)
        print(glass2)
    except (TypeError, ValueError) as e:
        print(f"Error while creating a valid Glass object: {e}")

        # Некорректные объекты
    try:
        glass_invalid1 = Glass("500", 300)  # Некорректный тип capacity_volume
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")

    try:
        glass_invalid2 = Glass(500, -100)  # Отрицательный объем
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")

    try:
        glass_invalid3 = Glass(500, 600)  # Заполнено больше, чем вместимость
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")

    try:
        glass_invalid4 = Glass(0, 100)  # Нулевая вместимость
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
