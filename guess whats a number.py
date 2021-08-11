import numpy as np

count = 0  # счетчик попыток
number = np.random.randint(1, 101)  # загадали число

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)

def game_core(number):
    '''Сначала устанавливаем любое random число, а потом действуем по алгоритму сужения границ:
    если random число больше, то нижней границей становится наше предположение и новое предположение рассчитывается как
    сумма верхней границы (на начальном этапе 100) с нижней границей, деленная пополам плюс 1;
    обратная ситуация, если random число меньше (наше предположение становится верхней границей)'''
    count = 1
    min_range = 1
    max_range = 101
    predict = (max_range + min_range) // 2
    while number != predict:
        count += 1
        if number > predict:
            min_range = predict
        elif number < predict:
            max_range = predict
        predict = (max_range + min_range) // 2

    return (count)  # выход из цикла, если угадали

score_game(game_core)