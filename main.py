from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD
from machine import Pin

firmware_url = "https://github.com/tomtommahout/test_ota"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "test.py")
ota_updater.download_and_install_update_if_available()


led = Pin(25, Pin.OUT)

led.toggle()
