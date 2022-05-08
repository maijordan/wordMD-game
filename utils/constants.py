import arcade 

#window constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "wordMD"

#style constants
FONT_NAME = "Kenney High"
READABLE_FONT_NAME = "Kenney Pixel"
BKGRD_COLOR = arcade.csscolor.DARK_SLATE_GRAY
INFECTED_COUNT_COLOR = arcade.make_transparent_color(arcade.color.ARSENIC, 200)

#score constants
SCORE_FILE = "scores.txt"

#title sprite constants
TITLE_IMG = "resources/title_01.png"
TITLE_IMG_WIDTH = 350

#player sprite constants
PLAYER_IMG = "resources/ambulance_01.png"
PLAYER_IMG_SCALE = 0.05

#bullet sprite constants
BULLET_IMG = "resources/syringe_01.png"
BULLET_IMG_SCALE = 0.02

#letter sprite constants
LETTER_IMG_FOLDER = "resources/letters/zombie/"
LETTER_IMG_SCALE = 0.25
LETTER_SPACING = 55
LETTER_SPAWN_HEIGHT = -20
HEALTH_BAR_OFFSET = 30

#background sprite constants
ROAD_IMG = "resources/road_01.png"
LEFT_BARRIER = 155
RIGHT_BARRIER = 845

#audio constants
MUSIC_VOL = 0.1
BKGRD_MUSIC = "resources/sounds/driftveil.mp3"
GUN_SOUND = arcade.load_sound(":resources:sounds/hurt4.wav")
GUN_SOUND_VOL = 0.1
CORRECT_SOUND = arcade.load_sound("resources/sounds/correct.mp3")
INCORRECT_SOUND = arcade.load_sound(":resources:sounds/hurt3.wav")

#difficulty constants
NUM_LIVES = 3
MIN_LETTERS = 3
MAX_LETTERS = 5
MIN_INFECTED = 1
MAX_INFECTED = 2
MAX_LETTER_HEALTH = 30
BULLET_DMG = -1  #always negative
PT_MULT = 100

#speed constants
PLAYER_SPEED = 5
BULLET_SPEED = 46
BKGRD_SCROLL_SPEED = -5 #always negative
LETTER_SPEED = -1 #always negative

