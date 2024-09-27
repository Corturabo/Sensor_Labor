import time
import board
import adafruit_tsl2591
import csv


i2c = board.I2C()  


sensor = adafruit_tsl2591.TSL2591(i2c)


with open('tsl2591_data.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Total Light', 'Infrared Light', 'Visible Light', 'Full Spectrum'])

    
    writer.writerow(['Total Light', 'Infrared Light', 'Visible Light', 'Full Spectrum'])

    
    while True:
        try:
            lux = sensor.lux
            infrared = sensor.infrared
            visible = sensor.visible
            full_spectrum = sensor.full_spectrum
            
            print(f"Total light: {lux}lux")
            print(f"Infrared light: {infrared}")
            print(f"Visible light: {visible}")
            print(f"Full spectrum (IR + visible) light: {full_spectrum}")

            
            if lux <= 100000 and infrared <= 100000:
                with open('tsl2591_data.csv', 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([lux, infrared, visible, full_spectrum])

        
            time.sleep(1.0)

        except Exception:
            print("An error occurred")
