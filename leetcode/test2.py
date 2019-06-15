import win32gui
import win32print
from win32con import LOGPIXELSX, LOGPIXELSY

hwnd = win32gui.GetDesktopWindow()
desktop_dc = win32gui.GetDC(hwnd)
horizontal_dpi = win32print.GetDeviceCaps(desktop_dc, LOGPIXELSX)
vertical_dpi = win32print.GetDeviceCaps(desktop_dc, LOGPIXELSY)

dpi_dict = {96: 1, 120: 1.25, 144: 1.5, 192: 2}

scaling_value_horizontal = dpi_dict.get(horizontal_dpi)
scaling_value_vertical = dpi_dict.get(vertical_dpi)