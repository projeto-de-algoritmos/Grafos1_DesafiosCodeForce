a, b, c = map(int, input().split())

# declare integer sum

total = a  + b + c

if (total % 2 == 0):
  sum = total / 2
  
  x = sum - c
  y = sum - a
  z = sum - b
  
  if (x >= 0 and y >= 0 and z >= 0):
    print(int(x), int(y), int(z))
  else:
    print("Impossible")
else:
  print("Impossible")


