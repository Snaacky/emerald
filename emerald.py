import pymem
import pymem.process
import time

dwLocalPlayer = (0xAA9AB4)
m_flFlashMaxAlpha = (0xA2F4)

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_id, "client.dll").base_address

def main():
    print("Emerald has launched.")

    while True:
        try:
            player = pm.read_int(client + dwLocalPlayer)
            flash_value = player + m_flFlashMaxAlpha
            pm.write_float(flash_value, float(0))
            time.sleep(0.002)
        except pymem.exception.MemoryReadError:
            pass # Can happen if script loads before alive in-game.
        except pymem.exception.MemoryWriteError:
            pass # Same reason as above.

if __name__ == '__main__':
    main()
