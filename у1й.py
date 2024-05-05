BASE_FARE = 4.00
RATE_PER_KM = 0.25
DISTANCE_PER_RATE = 140

def taxi_payment(distance):
    distance_in_meters = distance * 1000
    fare = BASE_FARE + (distance_in_meters / DISTANCE_PER_RATE) * RATE_PER_KM
    return fare

# Расстояние поездки в километрах, умноженное на номер вашего варианта (7)
distance = 10 * 7
total_fare = taxi_payment(distance)

print(f"Итоговая сумма оплаты такси за поездку {distance} км: ${total_fare:.2f}")
