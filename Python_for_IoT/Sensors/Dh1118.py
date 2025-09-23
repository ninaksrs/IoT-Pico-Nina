import machine
import dht
import time

# ກຳນົດ Pin ທີ່ຕໍ່ກັບ DHT11
sensor = dht.DHT11(machine.Pin(22))  # ປ່ຽນເປັນ GPIO ຂອງທ່ານ

while True:
    try:
        sensor.measure()  # ສັ່ງໃຫ້ sensor ວັດຄ່າ
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temperature: {} C  Humidity: {}%".format(temp, hum))
    except Exception as e:
        print("Error:", e)
    time.sleep(2)  # ອ່ານຄ່າທຸກ 2 ວິນາທີ
