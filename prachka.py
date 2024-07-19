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
import arcade.gui as gui

records = [0,0,0,0,0,0,0,0,0,0]
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)

def readingRecords():
    global records
    with open("resources/records.txt", encoding="utf-8") as file:
        records.clear()
        for i in file:
            records.append(i)

class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()
class Game(arcade.Window):
    def __init__(self, width, height, title):
        self.inputer = False
        super().__init__(width, height, title, fullscreen=False, center_window=True)
        arcade.play_sound(arcade.load_sound('resources/videoplayback.m4a'), volume=0.02,looping=True)
        self.coinSound = arcade.load_sound('resources/smw_coin.wav')
        self.blockSound = arcade.load_sound('resources/smw_jump.wav')
        self.deadSound = arcade.load_sound('resources/smw_blargg.wav')
        self.finishSound = arcade.load_sound('resources/smw_cape_rise.wav')
        self.engine = all_maps.Engine()
        self.manager = gui.UIManager()
        self.engine.generateTheWay()
        self.hp = 4
        self.name = "Player"
        self.real_game = True
        self.score = 0
        self.current_score = 0
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
        if self.game and self.real_game:
            self.finishPlay = True
            print("сбросил inputer")
            self.hp-=1
            self.current_score = 0
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
                        self.score+=self.current_score
                        self.hp = 4
                        print("перегенерировал")
                        self.setup()
                        self.hero.to_stop()
                    else:
                        self.end_game = True
                else:
                    self.timer -= 0.1
                    if self.finishPlay:
                        arcade.play_sound(self.finishSound, volume=0.4)
                        self.finishPlay = False
                    arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH,SCREEN_HEIGHT,arcade.load_texture("resources/win/win.png"))
            else:
                if self.real_game:
                    arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH,
                                                  SCREEN_HEIGHT, arcade.load_texture("resources/win/lose.png"))
                    arcade.play_sound(self.deadSound, volume=0.2)
                    #lose
                else:
                    arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH,
                                                  SCREEN_HEIGHT, arcade.load_texture("resources/win/lose.png"))
                    arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 500, 450, arcade.color.DARK_BLUE_GRAY)

                ##########3
                readingRecords()
                for i in range(1, 11):
                    arcade.draw_text(records[10 - i], SCREEN_WIDTH * 9 / 11, SCREEN_HEIGHT / 3 + i * 20,
                                     color=(255, 255, 255))


            if self.end_game:
                arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                              arcade.load_texture("resources/win/win.png"))

        arcade.draw_text(str(self.score), 30, SCREEN_HEIGHT-50, color = arcade.color.RED_ORANGE, font_size=24 - int(self.score//100!=0)*8)
        arcade.draw_text('(+'+str(self.current_score)+")", 70, SCREEN_HEIGHT-50, color = arcade.color.BLUE_GREEN, font_size=24- int(self.score//100!=0)*8)
        for i in range(self.hp):
            arcade.draw_texture_rectangle(SCREEN_WIDTH-150+50*i, SCREEN_HEIGHT-50, 50,50,arcade.load_texture("resources/heart.png"))

        self.manager.draw()
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
        if self.hp <= 0:
            self.real_game = False
            self.game = False
            if not self.inputer:
                self.manager.enable()
                self.label = arcade.gui.UILabel(
                    text="Enter your name",
                    text_color=arcade.color.DARK_RED,
                    width=500,
                    height=40,
                    font_size=30,
                    font_name="Kenney Future",align='center')

                # Create an text input field
                self.input_field = gui.UIInputText(
                    text_color=(255,255,255),
                    font_size=24,
                    width=300,
                    text='Enter here...')

                # Create a button
                submit_button = gui.UIFlatButton(
                    color=arcade.color.DARK_BLUE_GRAY,
                    text='Save')
                # --- Method 2 for handling click events,
                # assign self.on_click_start as callback
                submit_button.on_click = self.on_click

                self.v_box = gui.UIBoxLayout()
                self.v_box.add(self.label.with_space_around(bottom=100))
                self.v_box.add(self.input_field.with_space_around(bottom=50, left=20))
                self.v_box.add(submit_button)
                self.v_box.add(QuitButton(text="Quit"))

                self.manager.add(
                    arcade.gui.UIAnchorWidget(
                        anchor_x="center_x",
                        anchor_y="center_y",
                        child=self.v_box)
                )
                print("вывел поле ввода")
                self.inputer=True


    def update_text(self):
        print(f"updating the label with input text '{self.input_field.text}'")
        self.name = self.input_field.text
        self.label.text = self.input_field.text

    def on_click(self, event):
        print(f"click-event caught: {event}")
        self.update_text()
        with open('resources/records.txt', 'w'):
            pass
        with open('resources/records.txt', 'a', encoding='utf-8') as file:
            k = 0
            change = False
            lastString = ''
            for i in records:
                fullString = ''
                k += 1
                if change and k <= 10:
                    fullString = lastString
                    lastString = i
                else:
                    j = 0
                    while (i[j] != ':'):
                        fullString += i[j]
                        j += 1

                    j += 1
                    fullString += ':'
                    bufer = ''
                    while (k <= 10 and j != len(i) - 1):
                        bufer += i[j]
                        j += 1
                    fullString += bufer + '\n'
                    bufer = int(bufer)
                    if bufer < self.score:
                        change = True
                        fullString = self.name + ":" + str(int(self.score)) + '\n'
                        lastString = i

                file.write(fullString)
            self.restart()

    def restart(self):
        self.inputer = False
        self.engine = all_maps.Engine()
        self.manager = gui.UIManager()
        self.engine.generateTheWay()
        self.hp = 4
        self.name = "Player"
        self.real_game = True
        self.score = 0
        self.current_score = 0
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
        # self.current_map = len(all_maps.maps)-1            ###CHANGE MAP
        self.setup()
    def on_key_press(self, key, modifiers):
        if key == arcade.key.H:
           self.restart()
        if self.game:

            if key == arcade.key.R:
                self.setup()
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
