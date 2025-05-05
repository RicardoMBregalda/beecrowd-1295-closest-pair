import math
import sys

def calcular_distancia(ponto1, ponto2):
    return math.hypot(ponto1[0] - ponto2[0], ponto1[1] - ponto2[1])

def menor_distancia_bruta(lista_pontos):
    menor_distancia = float('inf')
    quantidade_pontos = len(lista_pontos)
    for i in range(quantidade_pontos):
        for j in range(i + 1, quantidade_pontos):
            distancia_atual = calcular_distancia(lista_pontos[i], lista_pontos[j])
            if distancia_atual < menor_distancia:
                menor_distancia = distancia_atual
    return menor_distancia

def encontrar_menor_distancia(pontos_ordenados_x, pontos_ordenados_y):
    quantidade_pontos = len(pontos_ordenados_x)
    
    if quantidade_pontos <= 3:
        return menor_distancia_bruta(pontos_ordenados_x)
    
    indice_meio = quantidade_pontos // 2
    ponto_mediano = pontos_ordenados_x[indice_meio]
    
    pontos_esquerda_y = []
    pontos_direita_y = []
    for ponto in pontos_ordenados_y:
        if ponto[0] <= ponto_mediano[0]:
            pontos_esquerda_y.append(ponto)
        else:
            pontos_direita_y.append(ponto)
    
    distancia_esquerda = encontrar_menor_distancia(pontos_ordenados_x[:indice_meio], pontos_esquerda_y)
    distancia_direita = encontrar_menor_distancia(pontos_ordenados_x[indice_meio:], pontos_direita_y)
    
    menor_distancia = min(distancia_esquerda, distancia_direita)
    
    faixa_pontos = []
    for ponto in pontos_ordenados_y:
        if abs(ponto[0] - ponto_mediano[0]) < menor_distancia:
            faixa_pontos.append(ponto)
    
    tamanho_faixa = len(faixa_pontos)
    for i in range(tamanho_faixa):
        for j in range(i + 1, min(i + 7, tamanho_faixa)):
            distancia_faixa = calcular_distancia(faixa_pontos[i], faixa_pontos[j])
            if distancia_faixa < menor_distancia:
                menor_distancia = distancia_faixa
    
    return menor_distancia

def main():
    sys.setrecursionlimit(1 << 25)  # Ajusta o limite de recursão
    while True:
        try:
            entrada = sys.stdin.readline()
            if not entrada:
                break
            quantidade_pontos = int(entrada)
            if quantidade_pontos == 0:
                break
            lista_pontos = []
            for _ in range(quantidade_pontos):
                coordenada_x, coordenada_y = map(float, sys.stdin.readline().split())
                lista_pontos.append((coordenada_x, coordenada_y))
            
            pontos_ordenados_x = sorted(lista_pontos, key=lambda ponto: ponto[0])
            pontos_ordenados_y = sorted(lista_pontos, key=lambda ponto: ponto[1])
            
            distancia_minima = encontrar_menor_distancia(pontos_ordenados_x, pontos_ordenados_y)
            
            if distancia_minima >= 10000.0:
                print("INFINITY")
            else:
                print("{0:.4f}".format(distancia_minima))
        except:
            break

if __name__ == "__main__":
    main()
