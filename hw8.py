def buy(shopping_dict):
  item = input('상품을 입력하세요: ')
  if item == '':
    return False
  num = int(input('수량을 입력하세요: '))


  if item not in shopping_dict:
    shopping_dict[item] = num

  else:
    shopping_dict[item] += num

def show(shopping_dict):
  print(f'\n장바구니보기: {shopping_dict}')



def find(shopping_dict):
  print('\n[검색]')
  search_item = input('장바구니에서 확인하고자 하는 상품은? ')

  if search_item in shopping_dict:
    print(f'{search_item}(는) {shopping_dict[search_item]}개 담겨 있습니다.')
  else:
    print(f'장바구니에 {search_item}은(는) 없습니다.')



###### 주 프로그램 부 ######


shopping_bag = {}

while True:
  if buy(shopping_bag) == False:
    break

show(shopping_bag)
find(shopping_bag)