from manim import *
from manim_slides import Slide
from svgelements.svgelements import MutableSequence

def scene0(self: Slide):
    # Mobjects
    initial_values: MutableSequence =[0, 0, 0, 0, 0]
    random_values: MutableSequence =[27,18,9,15,31]
    likert_values: MutableSequence = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
    proposition = Text("Statement: 'The man must pay for everything on the first date.'", font_size=TEXT_SM, t2c={"Statement": BLUE})
    chart_likert = BarChart(
        values=initial_values,
        bar_names=likert_values,
        y_range=[-0.1, 0.1, 10],
        y_length=0.22,
        x_length=10,
        x_axis_config={"font_size": TEXT_SM},
    ).scale(1.2)

    proposition.to_edge(UP)

    self.play(Write(proposition))
    self.play(Write(chart_likert))

    self.wait(1)

    chart_random = BarChart(
        values=random_values,
        bar_names=likert_values,
        y_range=[0, 40, 10],
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": TEXT_SM},
    ).scale(0.9)

    self.play(Transform(chart_likert, chart_random))
    c_bar_lbls = chart_random.get_bar_labels(font_size=TEXT_SM)
    self.play(FadeIn(c_bar_lbls))

    self.next_slide()
    self.play(FadeOut(proposition), FadeOut(chart_likert), FadeOut(c_bar_lbls))
    # self.bring_to_back(self.background3)
