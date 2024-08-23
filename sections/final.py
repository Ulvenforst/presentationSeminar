from manim import *
from manim_slides import Slide

def final(self: Slide):
    final_text = Text("¡Gracias por su atención!", font_size=TEXT_LG)
    self.play(Write(final_text))
