import network
import uasyncio
# SSID - network name
# pwd - password
# attempts - how many time will we try to connect to WiFi in one cycle
# delay_in_msec - delay duration between attempts
async def WIFIConnect(hostname: str, SSID: str, pwd: str, attempts: int = 3, delay_in_msec: int = 200) -> network.WLAN:
    wlan = network.WLAN(net.STA_IF)
    wlan.active(True)
    #not working no clue why
    #wifi.config(dhcp_hostname = "PI-Pico")
    count = 1
    while not wlan.isconnected() and count <= attempts:
        print("WiFi connecting. Attempt {}.".format(count))
        if wlan.status() != net.STAT_CONNECTING:
            wlan.connect(SSID, pwd)
        await uasyncio.sleep_ms(delay_in_msec)
        count += 1
    if wlan.isconnected():
        print("ifconfig: {}".format(wlan.ifconfig()))
    else:
        print("Wifi not connected.")
    return wlan