from tabulate import tabulate
from random import randint


class Process:
    def __init__(self, time, enter_time=0):
        self.time = time
        self.enter_time = enter_time
        self.priority = randint(1, 4)
        self.time_at_start = time

    def __str__(self):
        return f'Время появления {self.enter_time}, время выполнения {self.time_at_start}, приоритет {self.priority}'


def sjf():
    def time_left():  # подсчёт оставшегося времени
        s = 0
        for i in proc_list:
            s += i.time
        return s

    def priority(lst, time):  # ищем следующий по приоритету процесс
        lst = sorted(lst, key=lambda p: p.time)
        lst = sorted(lst, key=lambda p: p.priority)
        for proc in lst:
            if time >= proc.enter_time and proc.time != 0:
                return proc

    # ввод количества процессов
    while True:
        try:
            number_of_processes = int(input("Введите количество процессов: "))
            break
        except:
            print("Некорректный ввод\n")

    # генерируем процессы
    proc_list = []
    for i in range(number_of_processes):
        enter_time = randint(0, 10)
        time = randint(1, 8)
        proc_list.append(Process(time, enter_time))

    table = [*[[] for _ in range(number_of_processes)]]
    pointer = 0
    total_waiting = 0
    total_processing = time_left()

    # сам алгоритм
    while time_left():
        proc = priority(proc_list, pointer)
        for i in range(len(table)):
            if proc_list[i] == proc:
                table[i].append("И")
                proc.time -= 1
            elif proc_list[i].enter_time <= pointer and proc_list[i].time != 0:
                table[i].append("Г")
                total_waiting += 1
            else:
                table[i].append("")
        pointer += 1
    table.insert(0, ["Время", *[i for i in range(1, pointer+1)]])
    for i in range(1, len(table)):
        table[i].insert(0, f"p{i-1}")

    # вывод
    print()
    for i, proc in enumerate(proc_list, 0):
        print(f"p{i}: {proc}")
    print(tabulate(table, tablefmt='simple'))
    print()
    print(f"Среднее время ожидания: {(total_waiting / number_of_processes):.2f}")
    print(f"Среднее полное время выполнения: {((total_waiting+total_processing) / number_of_processes):.2f}")
    return


if __name__ == "__main__":
    sjf()
