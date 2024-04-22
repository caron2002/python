def prod_set(num1, num2):

  for i in range(1, 10):
    for j in range(num1, num2+1):
      prod = j * i
      print(f'{j} X {i} = {prod:2d}', end = '\t') #일정한 간격을 띄우고자 할 때 \t 사용
    print("")
  print()

prod_set(2, 5)
prod_set(6, 9)