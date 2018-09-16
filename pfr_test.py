import pifacerelayplus
import time


def toggle_leds(pfr):
    for r in pfr.relays:
        r.toggle()
        time.sleep(1)


if __name__ == '__main__':
    # init board with 10 MHz spi speed
    pfr = pifacerelayplus.PiFaceRelayPlus(pifacerelayplus.RELAY, speed_hz=10000000)
    while True:
        toggle_leds(pfr)
