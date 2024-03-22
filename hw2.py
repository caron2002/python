def get_int_num(prompt) :
    num = int(input(prompt))
    return num

def exchange(cash) :
    n500 = cash // 500
    cash %= 500
    n100 = cash // 100
    cash %= 100
    n50 = cash // 50
    cash %= 50
    n10 = cash // 10
    print(f"500원 동전의 개수: {n500}")
    print(f"100원 동전의 개수: {n100}")
    print(f"50원 동전의 개수: {n50}")
    print(f"10원 동전의 개수: {n10}")

result1 = get_int_num("동전으로 교환하고자 하는 금액은? ")
exchange(result1)
