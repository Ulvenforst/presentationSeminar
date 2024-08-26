from manim import *
from manim_slides import Slide
from svgelements.svgelements import MutableSequence

def scene3(self: Slide):
    title = Text("Midiendo los ejemplos", font_size=TEXT_SM, color=BLUE)
    title.to_edge(UL)

    likert_values: MutableSequence =["TD", "D", "N", "A", "TA"]
    chart_range = [0, 60, 10]

    graph_scale = 0.6

    chart0_values: MutableSequence =[0,0,0,0,60]
    chart01_values: MutableSequence =[30,0,0,0,30]
    chart1_values: MutableSequence =[3,12,15,56,13]
    chart2_values: MutableSequence =[45,5,3,4,43]
    chart3_values: MutableSequence =[56,15,12,13,3]
    chart4_values: MutableSequence =chart3_values[::-1]
    chart5_values: MutableSequence =[0,50,0,0,50]
    chart6_values: MutableSequence =[25,25,0,0,50]
    chart7_values: MutableSequence =[25,0,50,0,25]
    chart8_values: MutableSequence =[25,10,30,10,25]

    pol_chart0 = Text("0%", font_size=TEXT_SM, color=GREY)
    pol_chart01 = Text("100%", font_size=TEXT_SM, color=GREY)
    pol_chart1 = Text("5.1%", font_size=TEXT_SM, color=GREY)
    pol_chart2 = Text("77.5%", font_size=TEXT_SM, color=GREY)
    pol_chart3 = Text("11%", font_size=TEXT_SM, color=GREY)
    pol_chart4 = Text("11%", font_size=TEXT_SM, color=GREY)
    pol_chart5 = Text("56.2%", font_size=TEXT_SM, color=GREY)
    pol_chart6 = Text("52.5%", font_size=TEXT_SM, color=GREY)
    pol_chart7 = Text("25%", font_size=TEXT_SM, color=GREY)
    pol_chart8 = Text("26%", font_size=TEXT_SM, color=GREY)

    chart_random0 = BarChart(
        values=chart0_values,
        bar_names=likert_values,
        y_range=chart_range,
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": TEXT_MD},
    ).scale(graph_scale)
    chart0_pol = Group(chart_random0, pol_chart0).arrange(DOWN, buff=0.5)

    chart_random01 = BarChart(
        values=chart01_values,
        bar_names=likert_values,
        y_range=chart_range,
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": TEXT_MD},
    ).scale(graph_scale)
    chart01_pol = Group(chart_random01, pol_chart01).arrange(DOWN, buff=0.5)

    charts0 = Group(chart0_pol, chart01_pol).arrange(RIGHT, buff=0.5)

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
    chart1_pol = Group(chart_random1, pol_chart1).arrange(DOWN, buff=0.5)

    chart_random2 = BarChart(
        values=chart2_values,
        bar_names=likert_values,
        y_range=chart_range,
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": TEXT_MD},
    ).scale(graph_scale)
    chart2_pol = Group(chart_random2, pol_chart2).arrange(DOWN, buff=0.5)

    charts1 = Group(chart1_pol, chart2_pol).arrange(RIGHT, buff=0.5)

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
    chart3_pol = Group(chart_random3, pol_chart3).arrange(DOWN, buff=0.5)

    chart_random4 = BarChart(
        values=chart4_values,
        bar_names=likert_values,
        y_range=chart_range,
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": TEXT_MD},
    ).scale(graph_scale)
    chart4_pol = Group(chart_random4, pol_chart4).arrange(DOWN, buff=0.5)

    charts2 = Group(chart3_pol, chart4_pol).arrange(RIGHT, buff=0.5)

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
    chart5_pol = Group(chart_random5, pol_chart5).arrange(DOWN, buff=0.5)

    chart_random6 = BarChart(
        values=chart6_values,
        bar_names=likert_values,
        y_range=chart_range,
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": TEXT_MD},
    ).scale(graph_scale)
    chart6_pol = Group(chart_random6, pol_chart6).arrange(DOWN, buff=0.5)

    charts3 = Group(chart5_pol, chart6_pol).arrange(RIGHT, buff=0.5)

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
    chart7_pol = Group(chart_random7, pol_chart7).arrange(DOWN, buff=0.5)

    chart_random8 = BarChart(
        values=chart8_values,
        bar_names=likert_values,
        y_range=chart_range,
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": TEXT_MD},
    ).scale(graph_scale)
    chart8_pol = Group(chart_random8, pol_chart8).arrange(DOWN, buff=0.5)

    charts4 = Group(chart7_pol, chart8_pol).arrange(RIGHT, buff=0.5)

    c_bar_lbls7 = chart_random7.get_bar_labels(font_size=TEXT_SM)
    c_bar_lbls8 = chart_random8.get_bar_labels(font_size=TEXT_SM)

    self.play(Transform(charts0, charts4), Transform(c_bar_lbls0, c_bar_lbls7), Transform(c_bar_lbls01, c_bar_lbls8))

    self.next_slide()
    self.wipe([title, charts0, c_bar_lbls0, c_bar_lbls01])

