import arcade
from arcade import gui
from utils.constants import FONT_NAME,TITLE_IMG,TITLE_IMG_WIDTH

class Style:
    primary_btn = {
        "font_name": (FONT_NAME,"calibri", "arial"),
        "font_size": 28,
        "font_color": arcade.color.WHITE,
        "border_width": 2,
        "border_color": None,
        "bg_color": arcade.csscolor.CORAL,
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
        "bg_color_pressed": arcade.color.LIGHT_GRAY,
        "border_color_pressed": arcade.color.WHITE,
        "font_color_pressed": arcade.color.WHITE_SMOKE,
    }


def genTitle():
    title = gui.UISpriteWidget(
            sprite=arcade.Sprite(TITLE_IMG), width=TITLE_IMG_WIDTH
        )
    return title.with_space_around(bottom=50)

def genBtn(title,onClick,isPrimary=True):
    btn = gui.UIFlatButton(
            text=title, width=200, style=(Style.primary_btn if isPrimary else Style.secondary_btn)
        )
    btn.on_click = onClick
    return btn.with_space_around(bottom=20)