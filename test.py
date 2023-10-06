var = int(input("몇단까지 입력할까요?"))
print(var, type(var))

def print_mulprtiplication_table(number):
    print(f"------[{number} 단]------")
    print("구구단을 출력합니다")
    for x in range(1, var+1):
        print("-----[" + str(x) + "단] -----")
        for y in range(1, var+1):
            print(x, "X", y, "=", x*y)

print_mulprtiplication_table(var)
