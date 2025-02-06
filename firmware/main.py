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

# key matrix
keyboard.matrix = MatrixScanner(
    cols=[board.GP27, board.GP28, board.GP29],
    rows=[board.GP02, board.GP01],
    diod_orientation=DiodeOrientation.COL2ROW
)

# rotary encoder
encoder = rotaryio.IncrementalEncoder(board.GP03, board.GP04)
encoderswitch = digitalio.DigitalInOut(board.GP12)
encoderswitch.direction = digitalio.Direction.INPUT
encoderswitch.pull = digitalio.Pull.UP
