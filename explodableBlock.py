import arcade
class ExplodableBlock(arcade.Sprite):
    def __init__(self,scale):
        super().__init__('resources/Blocks/meteor.png', 0.05 * scale )
        self.explodable = True