from datetime import datetime

def main():
  #Запрос имени и даты рождения у пользователя
  name = input("Введите ваше имя: ")
  birth_date_str = input("Введите вашу дату рождения (в формате ДД.ММ.ГГГГ): ")

  # Преобразование строки в дату
  birth_date = datetime.strptime(birth_date_str, "%d.%m.%Y")
  current_date = datetime.now()
  
  # Вычисление возраста в годах, месяцах и днях
  age_years = current_date.year - birth_date.year
  age_months = current_date.month - birth_date.month
  age_days = current_date.day - birth_date.day

  #Корректировка, если текущий месяц и день меньше месяца и дня рождения
  if age_days < 0:
    age_months -= 1
    age_days += (current_date.replace(month=current_date.month, day=1) - birth_date.replace(year=current_date.year, month=current_date.month, day=1)).days

  if age_months < 0:
    age_years -= 1
    age_months += 12

  # Вычисление общего количества прожитых дней и часов
  total_days_lived = (current_date - birth_date).days
  total_hours_lived = total_days_lived * 24
  
  # Вывод приветствия и расчетов
  print(f"Привет, {name}! Тебе {age_years} лет.")
  print(F"Ты прожил(а) примерно {age_years * 12 + age_months} месяцев, {total_days_lived} дней, {total_hours_lived} часов.")

if __name__ == "__main__":
  main()  