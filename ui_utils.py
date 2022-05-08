import arcade
from arcade import gui
from style import Style
from constants import TITLE_IMG,TITLE_IMG_WIDTH

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