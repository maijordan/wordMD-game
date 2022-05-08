import arcade
from arcade import gui
from style import Style
import views.game_start_view

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650

class GameInstructView(arcade.View):
	"""View to show game instructions"""

	def on_show(self):
		self.manager = gui.UIManager()
		self.manager.enable()

		arcade.set_background_color(arcade.csscolor.DARK_SLATE_GRAY)

		self.menu_grp = gui.UIBoxLayout()

		back_btn = gui.UIFlatButton(text="Back", width=200, style=Style.primary_btn)
		self.menu_grp.add(back_btn.with_space_around(top=445))
		back_btn.on_click = self.back

		self.manager.add(
            gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.menu_grp
            )
        )

	def on_draw(self):
		self.clear()
		
		arcade.draw_text("How to Play", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 120,
                        arcade.color.WHITE, font_size=50, anchor_x="center")
		arcade.draw_text("Random letters have infected words!", SCREEN_WIDTH / 2,
						SCREEN_HEIGHT - 200, arcade.color.WHITE, font_size=25, anchor_x="center")
		arcade.draw_text("Shoot the incorrect letters to save them!", SCREEN_WIDTH / 2,
						SCREEN_HEIGHT - 250, arcade.color.WHITE, font_size=25, anchor_x="center")
		arcade.draw_text("1. Use the right and left arrow keys or A and D to move the vehicle.",
						90, SCREEN_HEIGHT - 330, arcade.color.WHITE, font_size=20,
						anchor_x="left")
		arcade.draw_text("2. Hold the spacebar to shoot.",
						90, SCREEN_HEIGHT - 380, arcade.color.WHITE, font_size=20,
						anchor_x="left")
		arcade.draw_text("3. Hold Shift to show the number of remaining incorrect letters.",
						90, SCREEN_HEIGHT - 430, arcade.color.WHITE, font_size=20,
						anchor_x="left")
		arcade.draw_text("4. Press Esc to pause the game or return to the main menu.",
						90, SCREEN_HEIGHT - 480, arcade.color.WHITE, font_size=20,
						anchor_x="left")

		self.manager.draw()

	def back(self, event):
		print("Back to start screen")
		self.manager.disable()
		self.window.show_view(views.game_start_view.GameStartView())