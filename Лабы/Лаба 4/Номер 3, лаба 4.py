from tabulate import tabulate


def table(processes):
    table = [["Время", *[i for i in range(1, sum(processes.values()) + 1)]]]
    start = 0
    total_time = 0
    for i in processes.keys():
        time = processes[i]
        row = [f"P{i}"]
        row.extend(["Г"]*start + ["И"]*time)
        start = time + start
        total_time += start
        table.append(row)
    print(tabulate(table, tablefmt="grid"))
    print(f"Среднее время ожидания: {((total_time-sum(processes.values()))/len(processes)):.2f}")
    print("Полное время выполнения:", total_time)


def fcfs():
    while True:
        try:
            number_of_processes = int(input("Введите количество процессов: "))
            break
        except:
            print("Некорректный ввод\n")
    processes = {}
    i = 0
    while i < number_of_processes:
        try:
            time = int(input(f"Время исполнения {i}-го процесса: "))
            assert 1 <= time
            processes[i] = time
        except:
            print("Некорректный ввод")
            i -= 1
        i += 1
    print("\nПо порядку")
    table(processes)
    print("\nВ обратном порядке")
    table({k: v for k, v in sorted(processes.items(), reverse=True)})
    print("\nОптимальный порядок")
    table({k: v for k, v in sorted(processes.items(), key=lambda x: x[1])})
    return


if __name__ == "__main__":
    fcfs()

