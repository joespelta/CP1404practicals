from silver_service_taxi import SilverServiceTaxi

taxi_01 = SilverServiceTaxi("iTaxi", 120, 2)
taxi_02 = SilverServiceTaxi("Hummer", 200, 4)

taxi_01.drive(18)
taxi_02.drive(18)

print(taxi_01)
print(taxi_01.get_fare())
taxi_01.start_fare()
print(taxi_01)
print(taxi_01.get_fare())
print(taxi_02)
print(taxi_02.get_fare())
taxi_02.start_fare()
print(taxi_02)
print(taxi_02.get_fare())
