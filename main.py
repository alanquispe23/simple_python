# Listas por comprensión
def incrementa(x):
    return x*x

lista = [2,1,4,8,5,4,5,1,1,8]

a = [incrementa(x) for x in lista]

print(a)