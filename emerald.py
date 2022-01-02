"""
External NoFlash for CS:GO
"""
# Imports
import logging
import re
import time
import pymem


# CS:GO
pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll


# Offsets
def get_localplayer_offset() -> int:
    """Gets the dwLocalPlayer offset."""
    cs_bytes = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
    match_index = re.search(
        rb"\x8D\x34\x85....\x89\x15....\x8B\x41\x08\x8B\x48\x04\x83\xF9\xFF", cs_bytes
    ).start()
    return pm.read_int(client.lpBaseOfDll + match_index + 3) + 4 - client.lpBaseOfDll

dwLocalPlayer = get_localplayer_offset()
m_flFlashMaxAlpha = 0x1046C # don't know how to pattern search this


# Main Loop
def main() -> None:
    """Main loop for NoFlash"""
    logging.info("Emerald has started")
    while True:
        player = pm.read_int(client + dwLocalPlayer)
        if player:
            flash_value = player + m_flFlashMaxAlpha
            if flash_value:
                pm.write_float(flash_value, 0.0)

        time.sleep(1)


if __name__ == "__main__":
    main()
