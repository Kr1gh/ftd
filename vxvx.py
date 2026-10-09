import random

sarkanie = [1, 3 , 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

n = 100

while n > 0 and n < 1000000:
  l = float(input("cik liksi?: "))
  k = int(input("melns(1) vai sarkans(2):" ))
  while k > 2 and k < 1:
    k = int(input("melns(1) vai sarkans(2):" ))
  while l > n:
    print("neiesi parādā")
    l = float(input("cik liksi?: "))

  n = n - l
  a = random.randint(1, 36)
  if k == 1:
    if a not in sarkanie:
      l = l * 2
      n = n + l
      print("tev laba veiksma. tā arī turpini")
    print("palicis pāri:", n)
    print(a)
  else:
    if a in sarkanie:
      l = l * 2
      n = n + l
      print("tev laba veiksma. tā arī turpini")
    print("palicis pāri:", n)
    print(a)
  
if n <= 0:
  print("ej dirst")
else:
  print("malacis")
