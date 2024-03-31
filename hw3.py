def get_fixed_price(price, discount):
    discount = 100 - discount
    return int(price * (100 / discount))

discount = int(input('할인율은? '))
a_price = int(input('A 상품의 할인된 가격은? '))
b_price = int(input('B 상품의 할인된 가격은? '))

a_result = get_fixed_price(a_price, discount)
b_result = get_fixed_price(b_price, discount)

print(f"A 상품의 정가는 {a_result} 원")
print(f"B 상품의 정가는 {b_result} 원")

