a, b, c = sorted(map(int, input().split()))

# declare integer sum

sum = a  + b + c

if (sum % 2 == 0):
  sum = sum / 2
  
  x = sum - c
  y = sum - a
  z = sum - b
  
  if (x >= 0 and y >= 0 and z >= 0):
    print(int(x), int(y), int(z))
  else:
    print("Impossible\n")
else:
  print("Impossible\n")


