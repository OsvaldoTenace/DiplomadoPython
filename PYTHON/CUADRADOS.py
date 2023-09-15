def generar_cuadrados(N):
    lista = [x**2 for x in range(1,N)]
    return lista
    
N = int(input())

print(generar_cuadrados(N))