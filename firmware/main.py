import board
import digitalio
import rotaryio
import analogio
from kmk.kmk_keyboard import KMKKEYBOARD
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.extensions.peg_oled_display import Oled, OledDisplayMode, OledData
from kmk.handlers.stock import simple_key_sequence

keyboard = KMKKEYBOARD()
