import math
from oktagon import oktagon

def main():
  NewOktagon = oktagon(10)
  perimeter, square = NewOktagon.Oktagon_data()
  radius_desc, square_desc = NewOktagon.described_circle()
  radius_inc, square_inc = NewOktagon.incribed_circle()
  print("Данные об октагоне")
  print(f"Периметр: {perimeter:.2f}")
  print(f"Площадь: {square:.2f}")
  print(f"\n--- Описанная окружность ---")
  print(f"Радиус: {radius_desc:.2f}")
  print(f"Площадь: {square_desc:.2f}")
  print(f"\n--- Вписанная окружность ---")
  print(f"Радиус: {radius_inc:.2f}")
  print(f"Площадь: {square_inc:.2f}")
  NewOktagon.draw()


if __name__=="__main__":
    main()





