from manim import *
from manim_slides import Slide

def scene6(self: Slide):
    title = Text("Implementation of a provisional package", font_size=TEXT_SM, color=BLUE)
    title.to_edge(UL)

    perf1_img = ImageMobject("media/images/perf1.jpeg")
    perf2_img = ImageMobject("media/images/perf2.jpeg").scale(0.6)

    perf_imgs = Group(perf1_img, perf2_img).arrange(RIGHT)

    self.play(Write(title))
    self.play(FadeIn(perf_imgs))


    self.next_slide()
    self.play(FadeOut(perf_imgs), FadeOut(title))


