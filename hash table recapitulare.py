def suma():
    dex = {"d":20, "e":40, "f":60}
    suma = 0
    cuv ="def"
    for i in range(len(cuv)):
        suma += dex[cuv[i]]
    print("Suma este:", suma)


def adunare():
    print("Introduceti un numar de doua cifre:")
    x = int(input())
    z = x // 10
    u = x % 10
    print("Numarul obtinut din adunarea sutelor si unitatilor este:", z+u)
    # print(24 // 10)
    # print(24 % 10)

def adunare2():
    print("Introduceti un numar de trei cifre:")
    x = int(input())
    z = x // 100
    u = x // 10 % 10
    y = x % 10
    print("Numarul obtinut din adunarea sutelor, zecilor si unitatilor:", z+u+y)
    # print(324 // 100)
    # print(324 // 10 % 10)
    # print(324 % 10)

def adunare3():
    print("Introduceti un numar de patru cifre:")
    x = int(input())
    a = x // 1000
    b = x // 100 % 10
    c = x // 10 % 10
    d = x % 10
    print("Numarul obtinut din adunarea miimilor, sutelor, zecilor si unitatilor:", a+b+c+d)

    # % restul
    # // se taie un numar, se rotunjeste
    # se fac in ordine, prima data // si dupa %








if __name__ == "__main__":
    # suma()
    # adunare()
    # adunare2()
    adunare3()


