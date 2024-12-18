import time
from Adafruit_IO import Client 
from sense_hat import SenseHat

aio = Client('jackh7405', 'aio_xPzj86KemCr4svaRFBcMlgGJy55u')

sense = SenseHat()

while True:
    accel_data = sense.get_accelerometer_raw()
    accel_x = accel_data['x']
    accel_y = accel_data['y']
    aio.send('acceleration-x', accel_x)
    aio.send('acceleration-y', accel_y)
    time.sleep(5)