from machine import Pin
import utime

# ກຳໜົດຂາ GPIO (ເຊື່ອມເຂົ້າກັບ IN ຂອງ Relay)
relay = Pin(4, Pin.OUT)

while True:
    print("Relay ON")
    relay.value(1)   # ຈ່າຍໄຟໃຫ້ກັບ Relay (ອຸປະກອນການທຳງານ)
    utime.sleep(2)

    print("Relay OFF")
    relay.value(0)   # ຕັດໄຟ Relay (ອຸປະກອນຫຍຸດທຳງານ)
    utime.sleep(2)
