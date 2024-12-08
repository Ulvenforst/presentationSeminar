from manim import *
from manim_slides import Slide

def presentation(self: Slide):
    # Mobjects
    # self.add(self.background1)
    # self.bring_to_back(self.background1)

    title = Text("Polarization Measurements", font_size=TEXT_LG*0.8, color=BLUE)
    description = Text("Investigative Practice 2024-II", font_size=TEXT_SM*1.1, line_spacing=0.5, slant=ITALIC)

    author = VGroup(
            Text("Juan Camilo Narváez Tascón (Estudiante UV)" ),
            Text("Juan Francisco D. Frías (PhD, Profesor UV)"),
            Text("Jesús A. Aranda (PhD, Profesor UV)"),
            Text("Frank D. Valencia (PhD, Profesor)"),
            ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).set_color(GRAY).scale(0.35)

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
    self.play( FadeOut(main_content), FadeOut(logos), FadeOut(author), FadeOut(logoPromueva))
