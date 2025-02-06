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

keyboard.keymap = [
#   [q, w, e, a, s, d]
#   [SW2, SW1, ROT, SW3, SW4, SW6]
    [KC.Q, KC.W, KC.LSHIFT, KC.A, KC.S, KC.D],
    [KC.LSHIFT, KC.UP, KC.ESC, KC.LEFT, KC.DOWN, KC.RIGHT],
    [KC.COLN, KC.J, KC.ESC, KC.H, KC.K, KC.L]
]

currentlayer = 0

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

# slider
slider = analogio.AnalogIn(board.GP26)

def getsliderval():
    return slider.value // 257

def adjustvol():
    volumelevel = getsliderval()
    keyboard.tap_key(KC.VOLU, volume_level // 25)

def rotaryhandler():
    global.currentlayer
    position = encoder.position
    if position > 0:
        currentlayer = min(currentlayer+1, len(keyboard.keymap)-1)
    elif position < 0:
        currentlayer = max(currentlayer-1, 0)
    keyboard.active_layers = [currentlayer]

keyboard.before_matrix_scan.append(adjustvol)
keyboard.before_matrix_scan.append(rotaryhandler)

if __name__ == "__main__":
    keyboard.go()
