#Функция для расчета суммы оплаты за поездку на такси.
def taxi_payment(distance):
    base_tariff = 4.00  # Базовый тариф
    rate_per_140m = 0.25  # Ставка за каждые 140 м

    # Расчет количества 140-метровых отрезков
    distance_in_meters = distance * 1000
    num_140m_segments = distance_in_meters / 140

    # Расчет итоговой суммы оплаты
    total_payment = base_tariff + rate_per_140m * num_140m_segments
    return total_payment

# Пример использования функции для расчета оплаты за поездку на такси
distance = float(input("Введите расстояние поездки (в километрах) умноженное на номер вашего варианта: "))
total_payment = taxi_payment(distance)
print("Итоговая сумма оплаты за поездку на такси: $", round(total_payment, 2))