def main():
  base_currency = input("Введите код вашей базовой валюты (например, USD): ").upper()
  target_currency = input("Введите код целевой валюты (например, EUR): ").upper()
  amount = float(input("Введите сумму для конвертации: "))
  exchange_rate = float(input(f"Введите курс {base_currency} к {target_currency}: "))
  converted_amount = amount * exchange_rate
  print(f"{amount} {base_currency} равно {converted_amount:.2f} {target_currency}")

if __name__ == "__main__":
  main()
  