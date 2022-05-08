import arcade
from constants import FONT_NAME


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
