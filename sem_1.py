def check_cow_status(currentSignal: float | int) -> str:
    """
    Определение температуры коровы по показанию датчика и проверка её состояния.
    Входные данные: currentSignal (float | int) - значение тока датчика в мА (4-20 мА)
    Выходные данные: str - текст с информацией о работе датчика и состоянии коровы
    """
    if type(currentSignal) not in (int, float) or type(currentSignal) == bool:
        raise TypeError("Неверный тип сигнала")

    if currentSignal < 0:
        raise ValueError("Сигнал не может иметь отрицательное значение")

    if currentSignal == 0:
        return "Получен сигнал 0mA, датчик выключен"

    if 0 < currentSignal <= 3.9 or currentSignal >= 20.1:
        return f"Получен сигнал {currentSignal}mA, датчик работает неправильно"

    pvMin = 0.0
    pvMax = 75.0
    currentTemperature = (currentSignal - 4) * (pvMax - pvMin) / (20 - 4) + pvMin

    if 37.5 <= currentTemperature <= 39.0:
        cowStatus = "состояние коровы нормальное"
    elif 35.0 <= currentTemperature <= 37.4:
        cowStatus = "корова замерзла, необходимо обогревание"
    elif 39.1 <= currentTemperature <= 39.5:
        cowStatus = "корова перегрелась, необходимо охлаждение"
    elif currentTemperature < 34.9:
        cowStatus = "требуется внимание (возможна неисправность датчика или плохое самочувствие коровы)"
    elif currentTemperature > 39.6:
        cowStatus = "необходимо срочно вызвать ветеринара, корова заболела"
    else:
        cowStatus = "состояние не удалось определить"

    return f"Сигнал датчика {currentSignal}mA, датчик исправен, температура {currentTemperature} градусов, {cowStatus}"

try:
    userInput = float(input("Введите данные датчика (ток в мА): "))
    print(check_cow_status(userInput))
except (ValueError, TypeError):
    print("Ошибка: введено некорректное значение!")