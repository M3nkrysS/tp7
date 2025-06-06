import arcade
from arcade.gui import (
    UIManager,
    UITextureButton,
    UIAnchorLayout,
    UIGridLayout,
)

from game_view import GameView

# Preload textures, because they are mostly used multiple times, so they are not
# loaded multiple times
TEX_RED_BUTTON_NORMAL = arcade.load_texture(":resources:gui_basic_assets/button/red_normal.png")
TEX_RED_BUTTON_HOVER = arcade.load_texture(":resources:gui_basic_assets/button/red_hover.png")
TEX_RED_BUTTON_PRESS = arcade.load_texture(":resources:gui_basic_assets/button/red_press.png")


class MenuView(arcade.View):
    def __init__(self):
        super().__init__()

        # Create a UIManager
        self.ui = UIManager()

        # create a grid layout
        grid = UIGridLayout(
            column_count=1,
            row_count=4,
            vertical_spacing=40

        )

        # Create an anchor layout, which can be used to position widgets on screen
        anchor = self.ui.add(UIAnchorLayout(children=[grid]))

        # Add multiple button switches to the other Views.
        button_new_game = anchor.add(
            UITextureButton(
                text="New Game",
                texture=TEX_RED_BUTTON_NORMAL,
                texture_hovered=TEX_RED_BUTTON_HOVER,
                texture_pressed=TEX_RED_BUTTON_PRESS,
            )
        )
        grid.add(button_new_game, column=0, row=0)

        button_leaderboard = anchor.add(
            UITextureButton(
                text="Leaderboard",
                texture=TEX_RED_BUTTON_NORMAL,
                texture_hovered=TEX_RED_BUTTON_HOVER,
                texture_pressed=TEX_RED_BUTTON_PRESS,
            )
        )
        grid.add(button_leaderboard, column=0, row=1)

        button_options = anchor.add(
            UITextureButton(
                text="options",
                texture=TEX_RED_BUTTON_NORMAL,
                texture_hovered=TEX_RED_BUTTON_HOVER,
                texture_pressed=TEX_RED_BUTTON_PRESS,
            )
        )
        grid.add(button_options, column=0, row=2)

        button_quit = anchor.add(
            UITextureButton(
                text="Quit Game",
                texture=TEX_RED_BUTTON_NORMAL,
                texture_hovered=TEX_RED_BUTTON_HOVER,
                texture_pressed=TEX_RED_BUTTON_PRESS,
            )
        )
        grid.add(button_quit, column=0, row=3)

        # add a button to switch to the Game view
        @button_new_game.event("on_click")
        def on_click(event):
            pass
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)

    def on_show_view(self) -> None:
        self.ui.enable()

    def on_hide_view(self) -> None:
        self.ui.disable()

    def on_draw(self):
        # Clear the screen
        self.clear(color=arcade.uicolor.BLUE_PETER_RIVER)

        # Add draw commands that should be below the UI
        # ...

        self.ui.draw()

        # Add draw commands that should be on top of the UI (uncommon)
        # ...
