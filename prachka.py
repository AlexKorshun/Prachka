import os
import sys
import arcade
import random
import all_maps
import hero_class
import explodableBlock
import solidBlock
from all_maps import maps
import finishClass
from constants import *

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, fullscreen=False)

        self.engine = all_maps.Engine()
        self.engine.generateTheWay()


        self.scale_of_map = 1
        all_maps.maps[0] = self.engine.map
        for i in self.engine.map:
            print(i)

        self.column_count = COLUMN_COUNT
        self.row_count = ROW_COUNT
        self.indent = 0
        # спрайтлисты
        self.solid_blocks = arcade.SpriteList()
        self.explodable_blocks = arcade.SpriteList()
        # спрайты
        self.hero = hero_class.Hero(PLAYER_SPEED, self)
        # поля
        self.game = True
        self.delay_moment = 0
        self.timer = 0
        self.end_game = False
        self.cell_width = CELL_WIDTH
        self.cell_height = CELL_HEIGHT

        # инициализация спрайтов

        self.current_map = 0
        #self.current_map = len(all_maps.maps)-1            ###CHANGE MAP
        self.setup()

    def setup(self):
        all_maps.maps[0] = self.engine.map
        self.hero.won = False
        user_x = 0
        user_y = 0
        self.scale_of_map = 13.36/(len(all_maps.maps[self.current_map][0]))
        self.row_count = len(all_maps.maps[self.current_map])
        self.column_count = len(all_maps.maps[self.current_map][0])
        self.cell_width = CELL_WIDTH * self.scale_of_map
        self.cell_height = CELL_HEIGHT * self.scale_of_map
        self.hero.change_scale(self.scale_of_map)
        for y in range(self.row_count):
            for x in range(self.column_count):
                if maps[self.current_map][self.row_count - y - 1][x] == 6:
                    user_x = x
                    user_y = y
                elif maps[self.current_map][self.row_count - y - 1][x] == 7:
                    self.finishSprite = finishClass.FnishBlock(self.scale_of_map)
                    self.finishSprite.set_position(justify_x(difference(x, self.cell_width), self.cell_width, self.column_count),
                                                   justify_y(difference(y, self.cell_height), self.cell_height, self.row_count))


                elif maps[self.current_map][self.row_count - y - 1][x] == 1:
                    solid_block = solidBlock.SolidBlock(self.scale_of_map)
                    solid_block.center_x = difference(x, self.cell_width)
                    solid_block.center_y = difference(y, self.cell_height)
                    self.solid_blocks.append(solid_block)
                elif random.randint(1, 3) == 1:
                    exp_block = explodableBlock.ExplodableBlock(self.scale_of_map)
                    exp_block.center_x = difference(x, self.cell_width)
                    exp_block.center_y = difference(y, self.cell_height)
                    self.explodable_blocks.append(exp_block)

        x = justify_x(difference(user_x, self.cell_width), self.cell_width, self.column_count)
        y = justify_y(difference(user_y, self.cell_height), self.cell_height, self.row_count)
        self.hero.set_position(x, y)



    def on_draw(self):
        self.clear()
        if self.game:
            arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,arcade.load_texture("resources/background.png"))

            self.solid_blocks.draw()
            self.explodable_blocks.draw()
            self.hero.draw()
            self.finishSprite.draw()
        else:
            if self.hero.won:
                if self.timer <= 0:
                    if self.current_map < len(all_maps.maps)-1:
                        self.game = True
                        self.timer = 0
                        self.explodable_blocks.clear()
                        self.solid_blocks.clear()

                        self.engine = all_maps.Engine()
                        self.engine.generateTheWay()
                        print("перегенерировал")


                        self.setup()
                        self.hero.to_stop()
                    else:
                        self.end_game = True
                else:
                    self.timer -= 0.1
                    arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH,SCREEN_HEIGHT,arcade.load_texture("resources/win/win.png"))
            else:
                arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH,
                                              SCREEN_HEIGHT, arcade.load_texture("resources/win/lose.png"))
            if self.end_game:
                arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                              arcade.load_texture("resources/win/win.png"))

    def update(self, delta_time):

        if self.game:
            self.hero.update_animation(delta_time)
            self.hero.update()
        elif not self.hero.won:
            if self.timer <= 0:
                self.game = True
                self.timer = 0
                self.explodable_blocks.clear()
                self.setup()
                self.hero.to_stop()
            else:
                self.timer -= 0.1

    def on_key_press(self, key, modifiers):
        if self.game:
            if key == arcade.key.LEFT:
                self.hero.to_left()
            elif key == arcade.key.RIGHT:
                self.hero.to_right()
            elif key == arcade.key.UP:
                self.hero.to_up()
            elif key == arcade.key.DOWN:
                self.hero.to_down()
            self.hero.costume_change()
        if key == arcade.key.ESCAPE or key == arcade.key.F11:
            arcade.close_window()


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
