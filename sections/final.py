from manim import *
from manim_slides import Slide

def final(self: Slide):
    title = Text("Future work", font_size=TEXT_SM, color=BLUE)
    title.to_edge(UL)


    blist = BulletedList("Demonstrate the best alpha and beta", "Formalize proofs of ER axioms for MEC", "Finish the polarization measurements paper", "Start the process of implementing our measures in SciPy")

    self.play(Write(title), Write(blist))

