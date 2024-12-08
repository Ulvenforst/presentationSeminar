from manim import *
from manim_slides import Slide
from svgelements.svgelements import MutableSequence

def scene3(self: Slide):
    title = Text("Some general rules", font_size=TEXT_SM, color=BLUE)
    title.to_edge(UL)

    axiom1_png = ImageMobject("media/images/axiom1.png")
    axiom2_png = ImageMobject("media/images/axiom2.png")
    axiom3_png = ImageMobject("media/images/axiom3.png")

    axioms = Group(axiom1_png, axiom2_png, axiom3_png).arrange(RIGHT, buff=0.2)
    
    self.play(Write(title))
    self.play(FadeIn(axioms))

    self.next_slide()
    self.play(FadeOut(title), FadeOut(axioms))

    title2 = Text("Polarization measures", font_size=TEXT_SM, color=BLUE)
    title2.to_edge(UL)

    estebanRay = MathTex(r"\text{ER}_{\alpha}(M)=K \sum _{i=1}^n \sum _{j=1}^n \pi _{i}^{1+\alpha}\pi _{j} |x_i-x_j|").scale(0.7)
    emd = MathTex(r"\mathrm{EMD}_\text{pol}(M)=0.5-\mathrm{EMD}(M,\pi_{\max})").scale(0.7)
    shannon = MathTex(r"\text{Shannon}_{\text{pol}}(M) = -\sum_{i=1}^{n} \pi_i \log_2 \left( 1 - \frac{|x_i - \mu_{\vec{x}}|}{x_{\max} - x_{\min}} \right)").scale(0.7)
    eijk = MathTex(r"\mathrm{Eijk}_{\text{pol}}(M) = 1- \sum_{i=1}^n \pi_i \cdot A_i").scale(0.7)
    
    pol_measures = VGroup(estebanRay, emd, shannon, eijk).arrange(DOWN, buff=0.5)

    self.play(Write(title2), Write(pol_measures))

    self.next_slide()

    self.play(FadeOut(pol_measures))

    # Nueva escena con la definición en inglés
    intro_text = Text("""
                    Polarization is the minimum work required
                    to bring the entire population to consensus.
                    """, font_size=TEXT_SM, line_spacing=0.8)
    formal_definition = MathTex(r"\text{MEC}_{\alpha,\beta}(M) = \min_{x_p} \sum_{i=1}^n \pi_{i}^\alpha |x_i-x_p|^\beta", font_size=TEXT_MD)
    source3 = Text("Our definition: MEC", font_size=TEXT_XS, color=GREY)

    our_definition = VGroup(intro_text, formal_definition, source3).arrange(DOWN, buff=0.3, aligned_edge=LEFT)

    positions = VGroup(
            MathTex(r"x_1"), MathTex(r"x_2"), MathTex(r"x_3"), MathTex(r"x_4"), MathTex(r"x_5")
            ).arrange(RIGHT, buff=1.25).scale(0.6).shift(DOWN * 1.75, RIGHT * 3.4)

    pi2 = MathTex(r"\pi_2").set_color(PURPLE).scale(0.6).shift(DOWN*0.48 , RIGHT * 2.4)
    pi3 = MathTex(r"\pi_3").set_color(PINK).scale(0.6).shift(UP*0.27,RIGHT * 3.4)
    pi5 = MathTex(r"\pi_5").set_color(YELLOW).scale(0.6).shift(DOWN*0.48 , RIGHT * 5.4)

    p_cons = MathTex(r"p").set_color(PINK).scale(0.6).shift(UP*1.78 , RIGHT * 3.4)

    chart_range = [0, 100, 25]
    graph_scale = 0.5
    chart1_values: MutableSequence = [0,25,50,0,25]
    values_consensus: MutableSequence = [0,0,100,0,0]
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

    self.play(Write(our_definition))
    self.play(our_definition.animate.scale(0.8).next_to(chart_random1, LEFT, buff=0.5))
    self.play(Write(chart_random1), Write(positions), Write(pi2), Write(pi3), Write(pi5))

    self.next_slide()

    self.play(Transform(chart_random1, chart_consensus), Transform(pi2, p_cons), Transform(pi3, p_cons), Transform(pi5, p_cons))

    self.next_slide()

    # Mostrar todas las medidas incluyendo las nuevas
    bipol = MathTex(r"\text{BiPol}(M) := 4 \max_{A \cap B=\emptyset, A \cup B={x_1,...,x_n}} \dfrac{1}{n^2} \sum_{x \in A} \sum_{y \in B} |y-x|").scale(0.7)
    mec = MathTex(r"\text{MEC}_{\alpha,\beta}(M) = \min_{x_p} \sum_{i=1}^n \pi_{i}^\alpha |x_i-x_p|^\beta").scale(0.7)

    all_measures = VGroup(estebanRay, emd, shannon, eijk, mec, bipol).arrange(DOWN, buff=0.5).scale(0.8)

    self.play(
        FadeOut(our_definition), 
        FadeOut(chart_random1), 
        FadeOut(positions), 
        FadeOut(pi2), 
        FadeOut(pi3),
        FadeOut(pi5), 
        FadeOut(p_cons)
    )
    
    self.play(Write(all_measures))

    self.next_slide()

    self.play(FadeOut(all_measures), FadeOut(title2))
