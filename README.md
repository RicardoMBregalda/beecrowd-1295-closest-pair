# 📌 Beecrowd 1295 — Problema dos Pares Mais Próximos

Este repositório contém a solução para o problema **1295 - Problema dos Pares Mais Próximos** da plataforma [Beecrowd](https://www.beecrowd.com.br/), implementado em **Python** com abordagem eficiente de **divisão e conquista** para encontrar a menor distância entre dois pontos em um plano bidimensional.

---

## 📋 Descrição do Problema

Dado um conjunto de pontos em um espaço 2D, o objetivo é encontrar a **menor distância** entre quaisquer dois pontos distintos. Caso não haja dois pontos com distância menor que 10.000 unidades, o programa deve retornar `"INFINITY"`.

### 📥 Entrada

- Vários casos de teste.
- Cada caso inicia com um inteiro `N` (0 ≤ N ≤ 10000) — o número de pontos.
- Em seguida, `N` linhas com dois valores: as coordenadas `X` e `Y` de cada ponto (0 ≤ X, Y < 40000).
- O fim da entrada é indicado por `N = 0`.

### 📤 Saída

- Para cada conjunto, imprima a menor distância com **4 casas decimais**.
- Se a menor distância for **maior ou igual a 10000**, imprima: `INFINITY`.

---

## 💡 Exemplo

### Entrada

```
3
0 0
10000 10000
20000 20000
5
0 2
6 67
43 71
39 107
189 140
0
```

### Saída

```
INFINITY
36.2215
```

---

## 🚀 Como Executar

1. Salve o código como `pares_mais_proximos.py`.
2. Execute no terminal:

```bash
python pares_mais_proximos.py
```

---

## 🧠 Estratégia Utilizada

- Utiliza o algoritmo de **Divisão e Conquista (Divide and Conquer)** com complexidade `O(n log n)`.
- Para instâncias com 3 pontos ou menos, utiliza comparação bruta.
- Divide os pontos ordenados por eixo X, calcula recursivamente as menores distâncias e verifica possíveis candidatos cruzando a linha de divisão.

---

## 📎 Requisitos

- Python 3.x

---

## 🏁 Resultado

O código é capaz de processar grandes quantidades de pontos (até 10.000) de forma eficiente e precisa, respeitando o limite de tempo estabelecido pela plataforma Beecrowd.

---

## ✍️ Autor

**Ricardo Bregalda**  
🔗 [GitHub](https://github.com/RicardoMBregalda) | [Beecrowd](https://judge.beecrowd.com/pt/profile/635895)
