import pymem
import pymem.process
import time

dwLocalPlayer = (0xAA9AB4)
m_flFlashMaxAlpha = (0xA2F4)
dwEntityList = (0x4A8473C)

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_id, "client.dll").base_address

def main():
    print("Emerald has launched.")

    while True:
        # check if player is in-game (if entity list exists)
        if pm.read_int(client + dwEntityList) > 0:
            player = pm.read_int(client + dwLocalPlayer)
            flash_value = player + m_flFlashMaxAlpha
            pm.write_float(flash_value, float(0))
        time.sleep(0.002)

if __name__ == '__main__':
    main()
