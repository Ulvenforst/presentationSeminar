from manim import *
from manim_slides import Slide

def scene5(self: Slide):
    title = Text("Correlation between measurements", font_size=TEXT_SM, color=BLUE)
    title.to_edge(UL)

    measures_corr_img = ImageMobject("media/images/measures_corr.jpg")

    self.play(Write(title))
    self.play(FadeIn(measures_corr_img))

    self.wait(2)

    self.play(measures_corr_img.animate.scale(0.9).to_edge(LEFT))
     
    result1 = MathTex(r"\text{MEC}_{1,1}(M) = \text{EMD}(M,\text{med}(M))").scale(0.5)
    result2 = MathTex(r"\text{EMD}(\text{med}(M),\pi_{\max})-\text{EMD}(M,\pi_{\max})=\text{EMD}(M,\text{med}(M))").scale(0.5)

    results = VGroup(result1, result2).arrange(DOWN, aligned_edge=LEFT).next_to(measures_corr_img, RIGHT)

    self.play(Write(results))

    self.next_slide()
    self.play(FadeOut(measures_corr_img), FadeOut(results), FadeOut(title))
    
    


