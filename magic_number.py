unused = {1, 2, 3, 4, 5, 6, 7, 8, 9}

def next(n, d):
  if (d > 9):
    print(n)
  else:
    global unused
    for i in unused:
      num = n*10 + i
      if (num % d == 0):
        unused.remove(i)
        next(num, d + 1)
        unused.add(i)

next(0, 1)
