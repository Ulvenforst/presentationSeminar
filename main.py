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

        # Scenes
        presentation(self)
        scene0(self)
        scene1(self)
        scene2(self)
        scene3(self)
        final(self)
