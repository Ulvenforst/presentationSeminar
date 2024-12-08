from manim import *
from manim_slides import Slide
from svgelements.svgelements import MutableSequence

def scene1(self: Slide):
    title = Text("Let's think about polarization", font_size=TEXT_SM, color=BLUE)
    title.to_edge(UL)

    likert_values: MutableSequence =["TD", "D", "N", "A", "TA"]
    chart_range = [0, 60, 10]

    graph_scale = 0.6

    chart0_values: MutableSequence =[20,20,20,20,20]
    chart01_values: MutableSequence =[0,50,0,50,0]
    chart1_values: MutableSequence =[0,50,0,50,0]
    chart2_values: MutableSequence =[50,0,0,0,50]
    chart3_values: MutableSequence =[33,0,33,0,33]
    chart4_values: MutableSequence =[9,0,45,0,45]
    chart5_values: MutableSequence =[30,0,33,0,36]
    chart6_values: MutableSequence =[6,0,45,0,49]
    chart7_values: MutableSequence =[25,0,25,0,50]
    chart8_values: MutableSequence =[0,50,0,0,50]
    chart9_values: MutableSequence =[45,0,45,0,10]
    chart10_values: MutableSequence =[0,90,0,0,10]

    chart_random0 = BarChart(
        values=chart0_values,
        bar_names=likert_values,
        y_range=chart_range,
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": TEXT_MD},
    ).scale(graph_scale)

    chart_random01 = BarChart(
        values=chart01_values,
        bar_names=likert_values,
        y_range=chart_range,
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": TEXT_MD},
    ).scale(graph_scale)

    charts0 = Group(chart_random0, chart_random01).arrange(RIGHT, buff=0.5)

    c_bar_lbls0 = chart_random0.get_bar_labels(font_size=TEXT_SM)
    c_bar_lbls01 = chart_random01.get_bar_labels(font_size=TEXT_SM)

    self.play(Write(title))
    self.play(FadeIn(charts0), FadeIn(c_bar_lbls0), FadeIn(c_bar_lbls01))

    self.next_slide()

    chart_random1 = BarChart(
        values=chart1_values,
        bar_names=likert_values,
        y_range=chart_range,
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": TEXT_MD},
    ).scale(graph_scale)

    chart_random2 = BarChart(
        values=chart2_values,
        bar_names=likert_values,
        y_range=chart_range,
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": TEXT_MD},
    ).scale(graph_scale)

    charts1 = Group(chart_random1, chart_random2).arrange(RIGHT, buff=0.5)

    c_bar_lbls1 = chart_random1.get_bar_labels(font_size=TEXT_SM)
    c_bar_lbls2 = chart_random2.get_bar_labels(font_size=TEXT_SM)

    self.play(Transform(charts0, charts1), Transform(c_bar_lbls0, c_bar_lbls1), Transform(c_bar_lbls01, c_bar_lbls2))

    self.next_slide()

    chart_random3 = BarChart(
        values=chart3_values,
        bar_names=likert_values,
        y_range=chart_range,
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": TEXT_MD},
    ).scale(graph_scale)

    chart_random4 = BarChart(
        values=chart4_values,
        bar_names=likert_values,
        y_range=chart_range,
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": TEXT_MD},
    ).scale(graph_scale)

    charts2 = Group(chart_random3, chart_random4).arrange(RIGHT, buff=0.5)

    c_bar_lbls3 = chart_random3.get_bar_labels(font_size=TEXT_SM)
    c_bar_lbls4 = chart_random4.get_bar_labels(font_size=TEXT_SM)

    self.play(Transform(charts0, charts2), Transform(c_bar_lbls0, c_bar_lbls3), Transform(c_bar_lbls01, c_bar_lbls4))

    self.next_slide()

    chart_random5 = BarChart(
        values=chart5_values,
        bar_names=likert_values,
        y_range=chart_range,
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": TEXT_MD},
    ).scale(graph_scale)

    chart_random6 = BarChart(
        values=chart6_values,
        bar_names=likert_values,
        y_range=chart_range,
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": TEXT_MD},
    ).scale(graph_scale)

    charts3 = Group(chart_random5, chart_random6).arrange(RIGHT, buff=0.5)

    c_bar_lbls5 = chart_random5.get_bar_labels(font_size=TEXT_SM)
    c_bar_lbls6 = chart_random6.get_bar_labels(font_size=TEXT_SM)

    self.play(Transform(charts0, charts3), Transform(c_bar_lbls0, c_bar_lbls5), Transform(c_bar_lbls01, c_bar_lbls6))

    self.next_slide()

    chart_random7 = BarChart(
        values=chart7_values,
        bar_names=likert_values,
        y_range=chart_range,
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": TEXT_MD},
    ).scale(graph_scale)

    chart_random8 = BarChart(
        values=chart8_values,
        bar_names=likert_values,
        y_range=chart_range,
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": TEXT_MD},
    ).scale(graph_scale)

    charts4 = Group(chart_random7, chart_random8).arrange(RIGHT, buff=0.5)

    c_bar_lbls7 = chart_random7.get_bar_labels(font_size=TEXT_SM)
    c_bar_lbls8 = chart_random8.get_bar_labels(font_size=TEXT_SM)

    self.play(Transform(charts0, charts4), Transform(c_bar_lbls0, c_bar_lbls7), Transform(c_bar_lbls01, c_bar_lbls8))

    self.next_slide()

    chart_random9 = BarChart(
        values=chart9_values,
        bar_names=likert_values,
        y_range=chart_range,
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": TEXT_MD},
    ).scale(graph_scale)

    chart_random10 = BarChart(
        values=chart10_values,
        bar_names=likert_values,
        y_range=chart_range,
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": TEXT_MD},
    ).scale(graph_scale)

    charts5 = Group(chart_random9, chart_random10).arrange(RIGHT, buff=0.5)

    c_bar_lbls9 = chart_random9.get_bar_labels(font_size=TEXT_SM)
    c_bar_lbls10 = chart_random10.get_bar_labels(font_size=TEXT_SM)

    self.play(Transform(charts0, charts5), Transform(c_bar_lbls0, c_bar_lbls9), Transform(c_bar_lbls01, c_bar_lbls10))

    self.next_slide()

    self.play(FadeOut(title), FadeOut(charts0), FadeOut(c_bar_lbls0), FadeOut(c_bar_lbls01))
