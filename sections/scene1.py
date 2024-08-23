from manim import *
from manim_slides import Slide
from svgelements.svgelements import MutableSequence

def scene1(self: Slide):
    title = Text("Más ejemplos", font_size=TEXT_SM, color=BLUE)
    title.to_edge(UP)

    likert_values: MutableSequence =["TD", "D", "N", "A", "TA"]
    chart_range = [0, 60, 10]

    graph_scale = 0.6

    chart1_values: MutableSequence =[3,12,15,56,13]
    chart2_values: MutableSequence =[45,5,3,4,43]
    chart3_values: MutableSequence =[56,15,12,13,3]
    chart4_values: MutableSequence =chart3_values[::-1]
    chart5_values: MutableSequence =[0,50,0,0,50]
    chart6_values: MutableSequence =[25,25,0,0,50]
    chart7_values: MutableSequence =[25,0,50,0,25]
    chart8_values: MutableSequence =[25,10,30,10,25]

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

    self.play(Write(title))
    self.play(FadeIn(charts1), FadeIn(c_bar_lbls1), FadeIn(c_bar_lbls2))

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

    self.play(Transform(charts1, charts2), Transform(c_bar_lbls1, c_bar_lbls3), Transform(c_bar_lbls2, c_bar_lbls4))

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

    self.play(Transform(charts1, charts3), Transform(c_bar_lbls1, c_bar_lbls5), Transform(c_bar_lbls2, c_bar_lbls6))

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

    self.play(Transform(charts1, charts4), Transform(c_bar_lbls1, c_bar_lbls7), Transform(c_bar_lbls2, c_bar_lbls8))

    self.next_slide()
    self.wipe([title,charts1, c_bar_lbls1, c_bar_lbls2])
