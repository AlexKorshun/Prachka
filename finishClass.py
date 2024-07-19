import arcade


class FnishBlock(arcade.Sprite):
    def __init__(self, scale):
        super().__init__('resources/Blocks/FinalBlock.png', scale)
        self.explodable = True
