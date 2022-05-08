import arcade
from arcade import gui
from utils.constants import FONT_NAME,TITLE_IMG,TITLE_IMG_WIDTH

class ButtonStyle:
    """holds button style configs"""

    primary_btn = {
        "font_name": (FONT_NAME,"calibri", "arial"),
        "font_size": 28,
        "font_color": arcade.color.WHITE,
        "border_width": 2,
        "border_color": None,
        "bg_color": arcade.csscolor.CORAL,
        
        #styles for when hover/press btn
        "bg_color_pressed": arcade.csscolor.LIGHT_CORAL,
        "border_color_pressed": arcade.color.WHITE,
        "font_color_pressed": arcade.color.WHITE_SMOKE,
    }

    secondary_btn = {
        "font_name": (FONT_NAME,"calibri", "arial"),
        "font_size": 28,
        "font_color": arcade.color.WHITE,
        "border_width": 2,
        "border_color": None,
        "bg_color": arcade.csscolor.GRAY,
        
        
        #styles for when hover/press btn
        "bg_color_pressed": arcade.color.LIGHT_GRAY,
        "border_color_pressed": arcade.color.WHITE,
        "font_color_pressed": arcade.color.WHITE_SMOKE,
    }


def genTitle():
    """Generates title widget with appropriate spacing"""
    title = gui.UISpriteWidget(
            sprite=arcade.Sprite(TITLE_IMG), width=TITLE_IMG_WIDTH
        )
    return title.with_space_around(bottom=50)

def genBtn(title,onClick,isPrimary=True):
    """Generates btn with appropriate spacing using title text, attaches onClick func, and sets style based on isPrimary flag"""
    btn = gui.UIFlatButton(
            text=title, width=200, style=(ButtonStyle.primary_btn if isPrimary else ButtonStyle.secondary_btn)
        )
    btn.on_click = onClick
    return btn.with_space_around(bottom=20)

def genLabel(title,isNum=False):
    """Generates label with appropriate spacing using title text, changes color if is a num"""
    label = arcade.gui.UILabel(text = str(title),font_size = 18,text_color=(arcade.color.BLUE_GREEN if isNum else arcade.color.WHITE))
    return label.with_space_around(bottom=10)
    