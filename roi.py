import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# определить функцию для минимизации
def function(x, y):
    return (x + 2*y -7) ** 2 + (2 * x + y - 5) ** 2

# Ограничения
bounds = [-10, 10]

# Задание параметров
num_particles = 20
max_iterations = 100
c1 = 2
c2 = 2
w = 0.1

# Инициализация частиц
particles_position = np.random.uniform(low=bounds[0], high=bounds[1], size=(num_particles, 2))
particles_velocity = np.zeros((num_particles, 2))
particles_best_position = particles_position.copy()
particles_best_value = np.array([function(x, y) for x, y in particles_position])

# Инициализация глобально лучшей частицы
global_best_index = np.argmin(particles_best_value)
global_best_position = particles_best_position[global_best_index]
global_best_value = particles_best_value[global_best_index]

# Тело алгоритма
for i in range(max_iterations):
    # Обновление скорости и позиции частиц
    r1 = np.random.uniform(size=(num_particles, 2))
    r2 = np.random.uniform(size=(num_particles, 2))
    particles_velocity = w * particles_velocity \
                        + c1 * r1 * (particles_best_position - particles_position) \
                        + c2 * r2 * (global_best_position - particles_position)
    particles_position = particles_position + particles_velocity
    
    # Проверка на ограничения
    particles_position = np.clip(particles_position, bounds[0], bounds[1])
    
    # Обновить лучшую позицию и значение частицы
    new_particles_best_value = np.array([function(x, y) for x, y in particles_position])
    mask = new_particles_best_value < particles_best_value
    particles_best_position[mask] = particles_position[mask]
    particles_best_value[mask] = new_particles_best_value[mask]
    
    # Обновить глобально лучшую позицию и значение
    global_best_index = np.argmin(particles_best_value)
    global_best_position = particles_best_position[global_best_index]
    global_best_value = particles_best_value[global_best_index]
    
# Вывод
    print('Итерация {}: Лучшее значение = {:.4f}, x = {:.4f}, y = {:.4f}'.format(i+1, global_best_value, global_best_position[0], global_best_position[1]))