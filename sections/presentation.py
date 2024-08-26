from manim import *
from manim_slides import Slide

def presentation(self: Slide):
    # Mobjects
    self.add(self.background1)
    self.bring_to_back(self.background1)

    title = Text("¿Cómo se mide la polarización?", font_size=TEXT_LG*0.8, color=BLUE)
    description = Text("Descubre cómo una app mide la polarización en\nlas redes sociales con precisión y rigor científico", font_size=TEXT_SM*1.1, line_spacing=0.5, slant=ITALIC)

    author = VGroup(
            Text("Jesús A. Aranda (PhD, Profesor UV)", font_size=TEXT_XS),
            Text("Joan Sebastian Betancourt (Investigador UV)", font_size=TEXT_XS),
            Text("Juan Camilo Narváez Tascón (Estudiante UV)", font_size=TEXT_XS)
            ).arrange(DOWN, buff=0.1, aligned_edge=LEFT).set_color(GRAY)

    logoUnivalle = ImageMobject("media/images/logoUnivalle.png").scale(0.43)
    logoAvispa = ImageMobject("media/images/logoAvispa.png").scale(0.9)
    logoPromueva = ImageMobject("media/images/logoPromueva.png").scale(0.18)
    logos = Group(logoUnivalle, logoAvispa, logoPromueva).arrange(RIGHT, buff=0.1).scale(0.8)

    # Styles

    # Positioning
    logos.to_edge(UL)
    author.to_edge(DL)

    main_content = VGroup(title, description).arrange(DOWN, buff=0.6, aligned_edge=LEFT)
    self.add(main_content, logos, author)

    main_content.to_edge(LEFT)

    self.wait()

    self.next_slide()
    self.play(FadeOut(self.background1), FadeIn(self.background2), FadeOut(main_content), FadeOut(logos), FadeOut(author), FadeOut(logoPromueva))
    self.bring_to_back(self.background2)
