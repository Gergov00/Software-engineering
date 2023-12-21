def lamb(T, p):
    return A0(T) + A1(T) * p


def A0(T):
    return 1316 - 5.692 * T + 6.83 * 10 ** (-3) * T ** 2


def A1(T):
    return -8.89 * 10 ** (-2) + 4.76 * 10 ** (-3) * T - 5.68 * 10 ** (-7) * T ** 2


def read_input_from_console():
    T_start = int(input("Введите начальную температуру (в кельвинах): "))
    T_end = int(input("Введите конечную температуру (в кельвинах): "))
    T_step = int(input("Введите шаг температуры (в кельвинах): "))

    p_start = int(input("Введите начальное давление (в паскалях): "))
    p_end = int(input("Введите конечное давление (в паскалях): "))
    p_step = int(input("Введите шаг давления (в паскалях): "))

    return T_start, T_end, T_step, p_start, p_end, p_step


def read_input_from_file(file_path):
    print("В файле данные должны находится в таком порядке, если это не так испарвьте пожалуйста \nТ(начальная) Т(конечная) Т(шаг) \nP(начальная) P(конечная) P(шаг)")

    input("Если все верно нажите Enter")
    with open(file_path, 'r') as file:
        lines = file.readlines()
        T_start, T_end, T_step = map(int, lines[0].split())
        p_start, p_end, p_step = map(int, lines[1].split())
        return T_start, T_end, T_step, p_start, p_end, p_step


def write_results_to_file(results, output_file_path):
    with open(output_file_path, 'w') as file:
        file.write("Температура (T), Давление (p), Результат\n")
        for result in results:
            file.write(f"{result['T']}°C, {result['p']} atm, {result['result']} \n")


try:
    input_type = input("Выберите источник ввода (console/file): ").lower()

    if input_type == 'console':
        T_start, T_end, T_step, p_start, p_end, p_step = read_input_from_console()
    elif input_type == 'file':
        file_path = "input.txt"
        T_start, T_end, T_step, p_start, p_end, p_step = read_input_from_file(file_path)
    else:
        raise ValueError("Некорректный выбор источника ввода.")

    results = []

    for T in range(T_start, T_end + 1, T_step):
        for p in range(p_start, p_end + 1, p_step):
            result = {"T": T, "p": p, "result": int(lamb(T, p))}
            results.append(result)

    output_file_path = "output.txt"
    write_results_to_file(results, output_file_path)

    print("Результаты сохранены в файл:", output_file_path)

except FileNotFoundError:
    print("Ошибка: Файл не найден.")
except ValueError as ve:
    print(f"Ошибка ввода: {ve}")
except Exception as e:
    print(f"Произошла ошибка: {e}")