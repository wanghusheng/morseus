"""Morseus default settings and constants."""


from libmorse import UNIT


# Camera image and color processing options.
SECOND = 1000.0    # how much is a second in ms
UNIT = float(UNIT)    # default morse unit (explicit declare)
MONO_THRESHOLD = 200    # pixels above this are considered white
LIGHT_DARK_RATIO = 2.0    # minimum light vs. dark quantity in an image
MAX_FPS = 30    # maximum number of frames per second supported
FPS_FACTOR = 3    # multiplied with the lowest computed FPS value

# Sub-area of interest within the whole capture.
class AREA:
    # How smaller is comparing to original.
    RATIO = 0.2
    # Minimum and maximum width for a sub-area.
    class WIDTH:
        MIN = 100.0
        MAX = 200.0
