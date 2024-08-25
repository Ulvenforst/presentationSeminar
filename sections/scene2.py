from manim import *
from manim_slides import Slide
from svgelements.svgelements import MutableSequence

def scene2(self: Slide):
    title = Title("¿Qué es la polarización?", font_size=TEXT_MD).set_color(BLUE)
    text1 = Text("""
                 «En política, polarización es el fenómeno por el cual 
                 la opinión pública se divide en dos extremos opuestos»
                 """, font_size=TEXT_SM, line_spacing=0.8)
    source1 = Text("Wikipedia", font_size=TEXT_XS, color=GREY)
    definition1 = VGroup(text1, source1).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
    text2 = Text("""
                 «La polarización [...] se refiere al grado en que las 
                 opiniones sobre un asunto se oponen en relación con 
                 algún máximo teórico.»
                 """, font_size=TEXT_SM, line_spacing=0.8)
    source2 = Text("DiMaggio et al. (1996)", font_size=TEXT_XS, color=GREY)
    definition2 = VGroup(text2, source2).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
    definition1.next_to(definition2, UP, buff=0.5, aligned_edge=LEFT)
    
    definitions = VGroup(definition1, definition2)
    definitions.shift(DOWN * 1)
    
    self.play(Write(title))
    self.play(Write(definition1))
    self.play(Write(definition2))
    self.next_slide()

    self.play(Unwrite(definition1), Unwrite(definition2))
    our_text = Text("""
                    La polarización es el trabajo mínimo requerido 
                    para llevar a toda la población a un consenso.
                    """, font_size=TEXT_SM, line_spacing=0.8)
    formal_definition = MathTex(r"Pol(\pi) = min_{p} \sum_i^n \pi_i^\alpha |x_i-p|^\beta", font_size=TEXT_MD)
    source3 = Text("Nuestra definición: COMÉTÉ", font_size=TEXT_XS, color=GREY)

    our_definition = VGroup(our_text, formal_definition, source3).arrange(DOWN, buff=0.3, aligned_edge=LEFT)

    self.play(Write(our_definition))

    self.next_slide()

    positions = VGroup(
            MathTex(r"x_1"), MathTex(r"x_2"), MathTex(r"x_3"), MathTex(r"x_4"), MathTex(r"x_5")
            ).arrange(RIGHT, buff=1.25).scale(0.6).shift(DOWN * 1.75, RIGHT * 3.4)

    weights = VGroup(
            MathTex(r"\pi_1").set_opacity(0), MathTex(r"\pi_2").set_color(PURPLE), MathTex(r"\pi_3").set_color(PINK), MathTex(r"\pi_4").set_opacity(0), MathTex(r"\pi_5").set_color(YELLOW)
            ).arrange(RIGHT, buff=1.25).scale(0.6).shift(DOWN*1.1 , RIGHT * 3.4)
    weights2 = VGroup(
            MathTex(r"\pi_1").set_opacity(0), MathTex(r"\pi_2").set_opacity(0), MathTex(r"p").set_color(PINK), MathTex(r"\pi_4").set_opacity(0), MathTex(r"\pi_5").set_opacity(0)
            ).arrange(RIGHT, buff=1.25).scale(0.6).shift(DOWN*1.1 , RIGHT * 3.41)

    chart_range = [0, 100, 25]
    graph_scale = 0.5
    chart1_values: MutableSequence =[0,25,50,0,25]
    values_consensus: MutableSequence =[0,0,100,0,0]
    chart_random1 = BarChart(
        values=chart1_values,
        y_range=chart_range,
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": TEXT_MD},
    ).scale(graph_scale).shift(RIGHT * 3.6)
    chart_consensus = BarChart(
        values=values_consensus,
        y_range=chart_range,
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": TEXT_MD},
    ).scale(graph_scale).shift(RIGHT * 3.6)

    self.play(our_definition.animate.scale(0.8).next_to(chart_random1, LEFT, buff=0.5))
    self.play(Write(chart_random1), Write(positions), Write(weights))

    self.next_slide()

    self.play(Transform(chart_random1, chart_consensus), Transform(weights, weights2))

    self.next_slide()
    self.play(Unwrite(title), Unwrite(our_definition), FadeOut(chart_random1), FadeOut(positions), FadeOut(weights), FadeOut(weights2))
