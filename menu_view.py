import arcade
import game_constants as gc


class MenuView(arcade.View):
    def on_show_view(self):
        self.window.background_color = arcade.color.BLACK

    def on_draw(self):
        self.clear()
        n_g = arcade.Text("New Game", gc.SCREEN_WIDTH / 2, gc.SCREEN_HEIGHT * 0.75, arcade.color.WHITE_SMOKE,
                          anchor_x="center", anchor_y="center")

        n_g.draw()
        color = 0, 0, 0, 0
        n_g_clickbox = arcade.draw_lrbt_rectangle_filled(gc.SCREEN_WIDTH / 2 - 40, gc.SCREEN_WIDTH / 2 + 40,
                                                         gc.SCREEN_HEIGHT * 0.75 - 10, gc.SCREEN_HEIGHT * 0.75 + 10,
                                                         color)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if
