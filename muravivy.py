import random

NUM_CITIES = 5

dist = [
    [0, 1, 2, 3, 4],
    [1, 0, 2, 3, 4],
    [2, 2, 0, 3, 4],
    [3, 3, 3, 0, 4],
    [4, 4, 4, 4, 0]
]

pheromone = [
    [0, 0.2, 0.2, 0.2, 0.2],
    [0.2, 0, 0.2, 0.2, 0.2],
    [0.2, 0.2, 0, 0.2, 0.2],
    [0.2, 0.2, 0.2, 0, 0.2],
    [0.2, 0.2, 0.2, 0.2, 0]
]

visited = [False] * NUM_CITIES

best_one = 10000
best_way = []


def next_city(start_city):
    global visited  # Объявляем, что используем глобальную переменную visited
    total = 0.0
    probability = [0] * NUM_CITIES

    for i in range(NUM_CITIES):
        if not visited[i]:
            probability[i] = dist[start_city][i] * pheromone[start_city][i]
            total += probability[i]

    probability = [prob / total for prob in probability]

    ver = random.random()
    sum_prob = 0.0
    for i in range(NUM_CITIES):
        if not visited[i]:
            if sum_prob <= ver < (sum_prob + probability[i]):
                visited[i] = True
                return i
            else:
                sum_prob += probability[i]

    return -1


def new_pheromone():
    for i in range(len(ways)):
        for j in range(NUM_CITIES):
            if j < NUM_CITIES - 1:
                pheromone[ways[i][j]][ways[i][j + 1]] += 5 / dist[ways[i][j]][ways[i][j + 1]]
            else:
                # Обрабатываем возврат муравья в начальный город
                pheromone[ways[i][j]][ways[i][0]] += 5 / dist[ways[i][j]][ways[i][0]]



def old_pheromone():
    for i in range(5):
        for j in range(5):
            if i != j:
                pheromone[i][j] *= 0.6


ways = []


def method(murovei):
    global visited
    global best_one
    global best_way

    for _ in range(murovei):
        start_city = 0  # Начинаем с города 0
        visited = [False] * NUM_CITIES
        visited[start_city] = True
        way = [start_city]

        for _ in range(1, NUM_CITIES):
            start_city = next_city(start_city)
            way.append(start_city)

        way.append(0)  # Убеждаемся, что муравей вернется в город 0
        ways.append(way)

        total_distance = 0
        for i in range(len(ways)):
            distance = sum(dist[ways[i][j]][ways[i][j + 1]] for j in range(NUM_CITIES))
            if distance < best_one:
                best_one = distance
                best_way = ways[i]
                total_distance += distance

    new_pheromone()


def main():
    iteracia = int(input("Введите количество итераций: "))
    murovei = int(input("Введите количество муравьев: "))

    for _ in range(iteracia):
        method(murovei)


if __name__ == "__main__":
    main()
    print(ways)
    print(best_one)
    print(best_way)
