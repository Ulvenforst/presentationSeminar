from manim import * 
from manim_slides import Slide

from sections.presentation import presentation
from sections.scene0 import scene0
from sections.scene1 import scene1
from sections.scene2 import scene2
from sections.scene3 import scene3
from sections.final import final

class PresentationSeminar(Slide):
    def construct(self):
        # Defaults
        Text.set_default(font="Noto Sans")
        self.background1 = ImageMobject("media/images/bg1.png").scale(1).set_opacity(0.3)
        self.background2 = ImageMobject("media/images/bg2.png").scale(1).set_opacity(0.1)
        self.background3 = ImageMobject("media/images/bg3.png").scale(1).set_opacity(0.3)
        self.background4 = ImageMobject("media/images/bg4.png").scale(1).set_opacity(0.3)

        # Scenes
        presentation(self)
        scene0(self)
        scene1(self)
        scene2(self)
        scene3(self)
        final(self)
