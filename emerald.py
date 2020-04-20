import pymem
import pymem.process
import time

dwLocalPlayer = (0xD2FB84)
m_flFlashMaxAlpha = (0xA40C)

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client_panorama.dll").lpBaseOfDll


def main():
    print("Emerald has launched.")

    while True:
        player = pm.read_int(client + dwLocalPlayer)
        flash_value = player + m_flFlashMaxAlpha
        if flash_value:
            pm.write_float(flash_value, float(0))
            time.sleep(1)


if __name__ == '__main__':
    main()
