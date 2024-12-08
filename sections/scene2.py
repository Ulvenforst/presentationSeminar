from manim import *
from manim_slides import Slide
from svgelements.svgelements import MutableSequence

def scene2(self: Slide):
    title = Title("What is polarization?", font_size=TEXT_MD).set_color(BLUE)
    text1 = Text("""
                'As the struggle proceeds, the whole society breaks up more and more into
                two hostile camps, two great, directly antagonistic classes: bourgeoisie and
                proletariat. The classes polarize, so that they become internally more
                homogeneous and more and more sharply distinguished from one another
                in wealth and power'
                 """, font_size=TEXT_SM, line_spacing=0.8).scale(0.9)
    source1 = Text("Deutsch (1971, p. 44).", font_size=TEXT_XS, color=GREY)
    image1 = ImageMobject("media/images/aardappeleters.jpg").scale(0.15).shift(DOWN * 2)
    definition1 = VGroup(text1, source1).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
    definition1.next_to(image1, UP, buff=0.5)
    
    self.play(Write(title))
    self.play(Write(definition1))
    self.play(FadeIn(image1))
    self.next_slide()

    self.play(Unwrite(definition1), FadeOut(image1))

    intro_text = Text("""
                    Polarization occurs when a society can be grouped 
                    into clusters, where individuals within clusters 
                    are similar and between clusters are different.
                    """, font_size=TEXT_SM, line_spacing=0.8)
                    
    features = BulletedList(
        "High degree of homogeneity within each group",
        "High degree of heterogeneity across groups",
        "Small number of significantly sized groups",
        font_size=TEXT_SM*1.5,
        buff=0.3
    )
    
    source3 = Text("Esteban & Ray (1994)", font_size=TEXT_XS, color=GREY)

    our_definition = VGroup(intro_text, features, source3).arrange(DOWN, buff=0.3, aligned_edge=LEFT)

    self.play(Write(our_definition))

    self.wait(1)

    dist_def = MathTex(r"(\vec{x},\vec{\pi}) = (\langle x_1,\ldots,x_m \rangle,\langle \pi_1,\ldots,\pi_m \rangle) \in [0,1]^m \times \mathbb{N}^m").scale(0.53).shift(DOWN * 2.2, RIGHT * 3.4)

    positions = VGroup(
            MathTex(r"x_1"), MathTex(r"x_2"), MathTex(r"x_3"), MathTex(r"x_4"), MathTex(r"x_5")
            ).arrange(RIGHT, buff=1.25).scale(0.6).shift(DOWN * 1.75, RIGHT * 3.4)


    pi2 = MathTex(r"\pi_2").set_color(PURPLE).scale(0.6).shift(DOWN*0.48 , RIGHT * 2.4)
    pi3 = MathTex(r"\pi_3").set_color(PINK).scale(0.6).shift(UP*0.27,RIGHT * 3.4)
    pi5 = MathTex(r"\pi_5").set_color(YELLOW).scale(0.6).shift(DOWN*0.48 , RIGHT * 5.4)

    p_cons = MathTex(r"p").set_color(PINK).scale(0.6).shift(UP*1.78 , RIGHT * 3.4)

    chart_range = [0, 100, 25]
    graph_scale = 0.5
    chart1_values: MutableSequence =[0,25,50,0,25]
    chart_random1 = BarChart(
        values=chart1_values,
        y_range=chart_range,
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": TEXT_MD},
    ).scale(graph_scale).shift(RIGHT * 3.6)


    self.play(our_definition.animate.scale(0.75).next_to(chart_random1, LEFT, buff=0.5))
    self.play(Write(chart_random1), Write(positions), Write(pi2), Write(pi3), Write(pi5), Write(dist_def))

    self.next_slide()

    self.play(FadeOut(title), FadeOut(our_definition), FadeOut(chart_random1), FadeOut(positions), FadeOut(pi2), FadeOut(pi3),FadeOut(pi5), FadeOut(dist_def))
