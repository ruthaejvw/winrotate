import ctypes
import time
from enum import Enum
from ctypes import wintypes

class Orientation(Enum):
    LANDSCAPE = 0
    PORTRAIT = 1
    LANDSCAPE_FLIPPED = 2
    PORTRAIT_FLIPPED = 3

def set_display_orientation(orientation):
    dm = ctypes.create_string_buffer(148)
    dm[0:4] = b'\x00\x00\x00\x00'
    dm[4:8] = b'\x00\x00\x00\x00'
    ctypes.windll.user32.EnumDisplaySettingsW(None, 0, dm)
    dm[40:44] = bytes([orientation.value, 0, 0, 0])
    dm[104:108] = b'\x00\x00\x00\x00'
    
    return ctypes.windll.user32.ChangeDisplaySettingsW(dm, 0) == 0

def main():
    predefined_settings = {
        # Define your settings here
        # Example: (hour, minute): Orientation
        (9, 0): Orientation.LANDSCAPE,
        (12, 0): Orientation.PORTRAIT,
        (15, 0): Orientation.LANDSCAPE_FLIPPED,
        (18, 0): Orientation.PORTRAIT_FLIPPED
    }

    while True:
        current_time = time.localtime()
        current_hour, current_minute = current_time.tm_hour, current_time.tm_min
        
        for (hour, minute), orientation in predefined_settings.items():
            if current_hour == hour and current_minute == minute:
                set_display_orientation(orientation)
        
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()