import arcade
import game_constants as gc


class MenuView(arcade.View):
    def on_show_view(self):
        self.window.background_color = arcade.color.BLACK

    def on_draw(self):
        self.clear()
        n_g = arcade.Text("New Game", gc.SCREEN_WIDTH / 2, gc.SCREEN_HEIGHT * 0.75, arcade.color.WHITE_SMOKE)

        n_g.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if
