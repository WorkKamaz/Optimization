import random
import math


# Генерация начального решения (случайный порядок доставки заказов)
def generate_initial_solution(orders):
    return random.sample(orders, len(orders))


# Рассчет общего расстояния для данного маршрута доставки
def calculate_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        # Получаем индексы для текущего и следующего в маршруте
        current_order = route[i]
        next_order = route[i + 1]
        # Используем индексы для получения расстояния из матрицы расстояний
        distance_between_orders = distance_matrix[current_order][next_order]
        total_distance += distance_between_orders
    return total_distance


# Расчет текущего решения
def evaluate_solution(route, distance_matrix):
    return calculate_distance(route, distance_matrix)


# Метод отжига
def simulated_annealing(orders, initial_temperature, cooling_rate, distance_matrix):
    current_solution = generate_initial_solution(orders)
    current_distance = evaluate_solution(current_solution, distance_matrix)
    temperature = initial_temperature

    while temperature > 0.1:
        # Генерация нового решения (случайный обмен двух заказов в маршруте)
        new_solution = current_solution[:]
        order1, order2 = random.sample(range(len(orders)), 2)
        new_solution[order1], new_solution[order2] = new_solution[order2], new_solution[order1]
        new_distance = evaluate_solution(new_solution, distance_matrix)

        # Расчет вероятности принятия нового решения
        probability = math.exp((current_distance - new_distance) / temperature)


        # Принятие нового решения с вероятностью probability
        if random.random() < probability:
            current_solution = new_solution
            current_distance = new_distance

        # Уменьшение температуры
        temperature *= 1 - cooling_rate

    return current_solution, current_distance


# Пример использования метода отжига для оптимизации маршрутов доставки заказов
orders = ["Корм для собак Darsi", "Капучинатор Raygood", "Чайник электрический", "Книга Скотный Двор автор Д. Оруэлл", "Гирлянда РОСА"]
# Пример матрицы расстояний (по порядку заказов в списке)
distance_matrix = {
    "Корм для собак Darsi": {"Корм для собак Darsi": 0, "Книга Скотный Двор автор Д. Оруэлл": 30, "Капучинатор Raygood": 20, "Чайник электрический": 40, "Гирлянда РОСА": 25},
    "Книга Скотный Двор автор Д. Оруэлл": {"Корм для собак Darsi": 30, "Книга Скотный Двор автор Д. Оруэлл": 0, "Капучинатор Raygood": 35, "Чайник электрический": 50, "Гирлянда РОСА": 45},
    "Капучинатор Raygood": {"Корм для собак Darsi": 20, "Книга Скотный Двор автор Д. Оруэлл": 35, "Капучинатор Raygood": 0, "Чайник электрический": 30, "Гирлянда РОСА": 40},
    "Чайник электрический": {"Корм для собак Darsi": 40, "Книга Скотный Двор автор Д. Оруэлл": 50, "Капучинатор Raygood": 30, "Чайник электрический": 0, "Гирлянда РОСА": 35},
    "Гирлянда РОСА": {"Корм для собак Darsi": 25, "Книга Скотный Двор автор Д. Оруэлл": 45, "Капучинатор Raygood": 40, "Чайник электрический": 35, "Гирлянда РОСА": 0}
}

initial_temperature = 10000
cooling_rate = 0.001

optimal_route, optimal_distance = simulated_annealing(orders, initial_temperature, cooling_rate, distance_matrix)
print("Изначальный путь:", orders)
print("Изначальное расстояние:", calculate_distance(orders, distance_matrix))
print("Оптимальный путь:", optimal_route)
print("Оптимальное расстояние:", optimal_distance)