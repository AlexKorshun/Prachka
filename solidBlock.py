import arcade


class SolidBlock(arcade.Sprite):
    def __init__(self,scale):
        super().__init__('resources/Blocks/SolidBlock.png', scale)
        self.explodable = False
