from manim import *
from manim_slides import Slide

def presentation(self: Slide):
    # Mobjects
    title = VGroup(
            Text("¿Cómo se mide la polarización?", font_size=TEXT_LG, color=BLUE)
            ).arrange(DOWN, buff=0.3)

    description = Tex(r"Descubre cómo una app mide la polarización en\\las redes sociales con precisión y rigor científico")
    description.font_size = TEXT_MD

    author = VGroup(
            Text("Jesús A. Aranda (PhD, Profesor UV)", font_size=TEXT_XS),
            Text("Joan Sebastian Betancourt (Estudiante Ingeniería de Sistemas UV)", font_size=TEXT_XS)
            ).arrange(DOWN, buff=0.1, aligned_edge=LEFT).set_color(GRAY)

    logoUnivalle = ImageMobject("media/images/logoUnivalle.png").scale(0.43)
    logoAvispa = ImageMobject("media/images/logoAvispa.png").scale(0.9)
    logoPromueva = ImageMobject("media/images/logoPromueva.png").scale(0.18)
    logos = Group(logoUnivalle, logoAvispa, logoPromueva).arrange(RIGHT, buff=0.1).scale(0.8)

    # Styles

    # Positioning
    logos.to_edge(UR)
    author.to_edge(DL)

    main_content = VGroup(title, description).arrange(DOWN, buff=0.6)
    self.add(main_content, logos, author)

    self.wait()

    self.next_slide()
    self.play(FadeOut(main_content), FadeOut(logos), FadeOut(author))
