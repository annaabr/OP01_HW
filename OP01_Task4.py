def main():
  # Запрос длины и ширины у пользователя
  length = float(input("Введите длину прямоугольника: "))
  width = float(input("Введите ширину прямоугольника: "))

  # Вычисление площади прямоугольника
  area = length * width

  # Вывод результата на консоль
  print(f"Площадь прямоугольника: {area}")

if __name__ == "__main__":
  main()
