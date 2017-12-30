import keyboard
import pymem
import pymem.process
import time
from config import *

pm = pymem.Pymem("csgo.exe")


def main():
    print("Emerald has launched. Enable no-flash with {}.".format(flash_key))
    client = pymem.process.module_from_name(pm.process_id, "client.dll")
    player = client.base_address + dwLocalPlayer
    flash_value = pm.read_int(player) + m_flFlashMaxAlpha

    toggled = False

    while True:
        if keyboard.is_pressed(flash_key):
            if not toggled:
                toggled = True
                pm.write_float(flash_value, float(0))
                print("No-flash has been toggled on.")
                time.sleep(1)
            else:
                toggled = False
                pm.write_float(flash_value, float(255))
                print("No-flash has been toggled off.")
                time.sleep(1)

        time.sleep(0.1)  # Prevents RuntimeError


if __name__ == '__main__':
    main()
