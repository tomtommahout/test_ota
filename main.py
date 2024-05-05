from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD
from machine import Pin

firmware_url = "https://github.com/tomtommahout/test_ota/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
ota_updater.download_and_install_update_if_available()

led = machine.Pin("LED", machine.Pin.OUT)
while True:
  led.value(True)  #turn on the LED
  time.sleep(1)   #wait for one second
  led.value(False)  #turn off the LED
  time.sleep(1)   #wait for one second
