shopping_bag = {}

print('[구입]')

while True:
  item = input('상품명? ')

  if item == "":
    break

  num = int(input('수량은? '))
  shopping_bag[item] = num
  print(f'장바구니에 사과 {num}개가 담겼습니다.')

print()
print(f'>>>장바구니 보기: {shopping_bag}')

print('\n[검색]')
search_item = input('장바구니에서 확인하고자 하는 상품은? ')
if search_item in shopping_bag:
  print(f"{search_item}은(는) {shopping_bag[search_item]}개 담겨 있습니다")
else:
  print('장바구니에 없는 목록입니다.')