from manim import *
from manim_slides import Slide
from svgelements.svgelements import MutableSequence

def scene4(self: Slide):
    title = Text("60 expert opinions", font_size=TEXT_SM, color=BLUE)
    title.to_edge(UL)

    # Configuración común
    chart_range = [0, 50, 10]
    graph_scale = 0.4
    x_values: MutableSequence = ["1", "2", "3", "4", "5"]

    # Definir todas las distribuciones
    dist1_values: MutableSequence = [12, 20, 40, 21, 7]
    dist2_values: MutableSequence = [40, 11, 28, 19, 2]
    dist3_values: MutableSequence = [2, 8, 44, 9, 1]
    dist4_values: MutableSequence = [20, 25, 2, 28, 25]
    dist5_values: MutableSequence = [3, 11, 17, 24, 44]
    dist6_values: MutableSequence = [44, 25, 16, 10, 4]
    dist7_values: MutableSequence = [2, 31, 8, 29, 30]
    dist8_values: MutableSequence = [7, 38, 8, 37, 10]
    dist9_values: MutableSequence = [21, 19, 19, 20, 21]
    dist10_values: MutableSequence = [3, 25, 44, 24, 3]
    dist11_values: MutableSequence = [36, 20, 27, 11, 6]
    dist12_values: MutableSequence = [1, 30, 37, 21, 11]
    dist13_values: MutableSequence = [15, 21, 30, 20, 14]
    dist14_values: MutableSequence = [36, 10, 8, 11, 35]
    dist15_values: MutableSequence = [10, 21, 38, 29, 2]

    # Crear VGroup para cada distribución
    distribution_groups = []
    for i, dist_values in enumerate([
        dist1_values, dist2_values, dist3_values, dist4_values, dist5_values,
        dist6_values, dist7_values, dist8_values, dist9_values, dist10_values,
        dist11_values, dist12_values, dist13_values, dist14_values, dist15_values
    ]):
        # Crear gráfico
        chart = BarChart(
            values=dist_values,
            bar_names=x_values,
            y_range=chart_range,
            y_length=2,
            x_length=3,
            x_axis_config={"font_size": 32}, 
            y_axis_config={"font_size": 32},
        ).scale(graph_scale)
        
        # Crear etiqueta
        label = Text(f"distribution {i+1}").scale(0.2)
        
        # Crear grupo para esta distribución
        dist_group = VGroup(chart, label).arrange(DOWN, buff=0.1)
        distribution_groups.append(dist_group)

    # Crear grid de distribuciones
    all_distributions = VGroup(*distribution_groups)
    all_distributions.arrange_in_grid(rows=5, cols=3, buff=0.2)

    # Animaciones iniciales
    self.play(Write(title))
    self.play(Create(all_distributions))
    
    self.next_slide()

    # Calculamos las nuevas posiciones
    right_side = VGroup(*distribution_groups).copy()
    right_side.arrange_in_grid(rows=5, cols=3, buff=0.2)
    right_side.shift(RIGHT * 3)
    positions_map = {i: right_side[i].get_center() for i in range(15)}
    
    # Reordenamos según original_order
    original_order = [3,10,1,12,13,15,5,6,9,11,2,7,8,4,14]
    reordered_positions = {original_order[i]-1: positions_map[i] for i in range(15)}
    
    # Crear fórmula y posicionarla a la izquierda
    formula = MathTex(
        r"\text{Experts}(M)=\frac{2.14\pi_2\pi_4 + 2.70(\pi_1\pi_4 + \pi_2\pi_5)+3.96\pi_1\pi_5}{0.0099\left(\sum_{i=1}^n\pi_i\right)^2}",
    ).scale(0.55)
    formula.shift(LEFT * 3.5)

    # Animar cada distribución a su nueva posición
    animations = []
    for i in range(15):
        animations.append(
            distribution_groups[i].animate.move_to(reordered_positions[i])
        )
    
    self.play(
        *animations,
        Write(formula)
    )

    self.next_slide()
    self.play(Unwrite(formula))

    correlations: MutableSequence = [1.000, 0.886, 0.867, 0.810, 0.771, 0.752, 0.752, 0.752, 0.676]
    measures: MutableSequence = ["RealMean", "ER(0,8)", "MEC(2,1)", "Experts", "BiPol", "Shannon", 
                               "MEC(1,1)", "EMD", "VanDerEijk"]

    # Crear gráfico de correlaciones
    correlation_chart = BarChart(
        values=correlations,
        bar_names=measures,
        y_range=[0, 1, 0.2],
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": 23},
    ).scale(0.57)

    correlation_chart_label = correlation_chart.get_bar_labels(font_size=18)

    correlation_title = Text("Correlation with experts ordering").scale(0.4)
    correlation_group = VGroup(correlation_title, correlation_chart).arrange(UP, buff=0.2)
    correlation_group.shift(LEFT * 3.5)
    correlation_chart_label.shift(LEFT * 3.15, UP * 0.25)

    self.play(
        FadeOut(formula),
        FadeIn(correlation_group),
        FadeIn(correlation_chart_label)
    )

    self.next_slide()


    # Definir nuevas correlaciones donde MEC(2,1) → MEC(2,1.15) con valor 0.886
    correlations_new: MutableSequence = [1.000, 0.886, 0.886, 0.810, 0.771, 0.752, 0.752, 0.752, 0.676]
    measures_new: MutableSequence = ["RealMean", "ER(0,8)", "MEC(2,1.15)", "Experts", "BiPol", "Shannon", 
                                   "MEC(1,1)", "EMD", "VanDerEijk"]

    correlation_chart_new = BarChart(
        values=correlations_new,
        bar_names=measures_new,
        y_range=[0, 1, 0.2],
        y_length=6,
        x_length=10,
        x_axis_config={"font_size": 23},
    ).scale(0.57)

    correlation_chart_label_new = correlation_chart_new.get_bar_labels(font_size=18)

    correlation_title_new = Text("Correlation with experts ordering").scale(0.4)
    correlation_group_new = VGroup(correlation_title_new, correlation_chart_new).arrange(UP, buff=0.2)
    correlation_group_new.shift(LEFT * 3.5)
    correlation_chart_label_new.shift(LEFT * 3.15, UP * 0.25)

    self.play(
        Transform(correlation_group, correlation_group_new),
        Transform(correlation_chart_label, correlation_chart_label_new)
    )

    self.next_slide()
    self.wipe([title, all_distributions, correlation_group, correlation_chart_label])

