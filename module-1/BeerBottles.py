def countdown(bottles):
  while bottles > 1:
      print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
      bottles = bottles - 1
      print(f"Take one down and pass it around, {bottles} bottle(s) of beer on the wall.")
      print()

  if bottles == 1:
      print("1 bottle of beer on the wall, 1 bottle of beer.")
      print("Take one down and pass it around, 0 bottles of beer on the wall.")
      print()


bottles = int(input("Enter number of bottles: "))

countdown(bottles)

print("Time to buy more bottles of beer.")