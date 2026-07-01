from manim import *


class Abertura(Scene):
    def construct(self):
        ponto = Dot([0, 0, 0])
        final = Dot([0,0,0])
        circulo = Circle(color=RED)
        circulo.set_fill(color=PURPLE, opacity=.5)
        rect = Rectangle(height=2.5, width=4)

        
        title = Text("You are")
        title.set_y(.7)
        gay = Text("Gay", color=PINK)
        gay.set_y(-.3)
        ass = Text("- Bernard T Schettini x0x0")
        ass.set_y(-1.3)

        self.play(FadeIn(ponto))
        self.wait()
        self.play(ReplacementTransform(ponto, circulo))
        self.wait(1)
        self.play(circulo.animate.shift(LEFT*3))
        self.wait(1)
        self.play(ReplacementTransform(circulo, rect), Write(title))
        self.play(Write(gay))
        self.wait(3)
        

        #self.play(Write(gay))
        #self.play(Write(ass))

        #self.play(FadeIn(rect))

        grupo = Group(gay, title, rect)
        self.play(ReplacementTransform(grupo,final))

        self.wait(1)
