import pifacerelayplus
import time


def toggle_leds(pfr):
    for r in pfr.relays:
        r.toggle()
        time.sleep(1)


if __name__ == '__main__':
    pfr = pifacerelayplus.PiFaceRelayPlus(pifacerelayplus.RELAY)
    while True:
        toggle_leds(pfr)

