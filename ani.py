#Animação para 28/08 sobre meu projeto AHP no ERMAC/Bombeiros

from manim import *

class e1(Scene):
    def construct(self):

        title = Paragraph("Seleção de Estudantes para um Projeto de",
                          "Pesquisa via o método AHP",
                         alignment="center")
        title.set_y(3)
        title.scale(.85)
        und = Underline(title)

        texto = Paragraph(
            "Há 1 bolsa de iniciação científica aberta, com certas características desejadas do aluno.",
            "Entre os 5 candidatos, qual será o melhor a ser escolhido?",
            alignment="center", 
            color=YELLOW,
            line_spacing=1.2
        ).scale(0.5)



        self.add(title, und)
        self.add(texto)



        
        self.wait(7)



class e2(Scene):
    def construct(self):
        # Title
        crit = Text("Características: Critérios e Subcritérios")
        crit.shift(UP*3).scale(0.6)

        # Items
        C1 = Text("1- Conhecimento Técnico", color=YELLOW).scale(0.45)
        C11 = Text("1.1- Experiência em Projetos de Pesquisa", color=YELLOW).scale(0.35)
        C12 = Text("1.2- Conhecimento em Ferramentas", color=YELLOW).scale(0.35)

        C2 = Text("2- Competência Comportamental", color=BLUE).scale(0.45)
        C21 = Text("2.1- Motivação/Interesse", color=BLUE).scale(0.35)
        C22 = Text("2.2- Disponibilidade de tempo", color=BLUE).scale(0.35)
        C23 = Text("2.3- Desenvoltura Social", color=BLUE).scale(0.35)

        # Group them vertically
        group1 = VGroup(C1, C11, C12).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        group1.next_to(crit, DOWN, buff=0.5).align_to(crit, LEFT)

        group2 = VGroup(C2, C21, C22, C23).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        group2.next_to(group1, DOWN, buff=0.5).align_to(crit, LEFT)
        
        # Add to scene
        self.add(crit, group1, group2)
        self.wait(10)

class e3(Scene):
    def construct(self):

        cand = Text("Avaliação dos Candidatos")
        cand.shift(UP*3).scale(.6)

        data = [
            ["10", "5", "9", "10", "9"],
            ["10", "0", "8", "10", "8"],
            ["10", "5", "10", "10", "10"],
            ["0",  "5", "8",  "10", "8"],
            ["10", "0", "10", "10", "10"]
        ]

        # Row labels
        row_labels=[Text("Candidato 1", font_size=24),
                    Text("Candidato 2", font_size=24),
                    Text("Candidato 3", font_size=24),
                    Text("Candidato 4", font_size=24),
                    Text("Candidato 5", font_size=24)
        ]

        # Column labels
        col_labels = [Text("1.1", font_size=24),
                      Text("1.2", font_size=24),
                      Text("2.1", font_size=24),
                      Text("2.2", font_size=24),
                      Text("2.3", font_size=24)
        ]

        # Create the table
        table = Table(
            data,
            row_labels=row_labels,
            col_labels=col_labels,
            top_left_entry=Text("Candidatos & Critérios", font_size=20),
            include_outer_lines=True,
            h_buff=1.2,
            v_buff=0.5
        ).scale(0.6)
        
        self.add(cand)
        self.play(Create(table))
        self.wait(7)

class e4(Scene):
    def construct(self):
        title = Text("Matrizes de Comparação")
        title.shift(UP*3).scale(.6)

        text = Text("Comparação entre os subcritérios", color=YELLOW)
        text.shift(UP*2.5).scale(.45)

        data = [
            ["1",   "1/3",   "1/8", "5",   "1/7"],
            ["3", "1",   "1/5", "7",   "1/3"],
            ["8",   "5",   "1",   "9",   "3"],
            ["5", "1/7", "1/9", "1",   "1/7"],
            ["7", "3",   "1/3", "7",   "1"]
        ]

        # labels
        col_labels = [Text("1.1"), 
                      Text("1.2"), 
                      Text("2.1"), 
                      Text("2.2"), 
                      Text("2.3")
        ]
        row_labels = [Text("1.1"), 
                      Text("1.2"), 
                      Text("2.1"), 
                      Text("2.2"), 
                      Text("2.3")
        ]
        # Create the table
        table = Table(
            data,
            row_labels=row_labels,
            col_labels=col_labels,
            top_left_entry=Text("Subcritérios", font_size=24),
            include_outer_lines=True,
            h_buff=1.2,
            v_buff=0.5
        ).scale(0.6)

        
        # Mostrando na tela
        self.add(title, text)
        self.play(Create(table))

        self.wait(7)
        
class e5(Scene):
    def construct(self):
        title = Text("Normalização")
        title.shift(UP*3).scale(.6)

        text = Text("Dividir cada elemento da matriz de comparação pela soma da coluna a que pertence ", color=YELLOW)
        text.shift(UP*2.5).scale(.45)

        data = [
            ["0.0520", "0.0351", "0.0706", "0.1724", "0.0309"],
            ["0.1562", "0.1055", "0.1130", "0.2413", "0.0721"],
            ["0.4166", "0.5276", "0.5651", "0.3103", "0.6494"],
            ["0.0104", "0.0150", "0.0627", "0.0344", "0.0309"],
            ["0.3645", "0.3165", "0.1883", "0.2413", "0.2164"],
        ]

        # Labels
        col_labels = [Text("1.1"), 
                      Text("1.2"), 
                      Text("2.1"), 
                      Text("2.2"), 
                      Text("2.3")
        ]
        row_labels = [Text("1.1"), 
                      Text("1.2"), 
                      Text("2.1"), 
                      Text("2.2"), 
                      Text("2.3")
        ]

        # Create the table
        table = Table(
            data,
            row_labels=row_labels,
            col_labels=col_labels,
            top_left_entry=Text("Subcritérios"),
            include_outer_lines=True,
            h_buff=0.9,
            v_buff=0.5
        ).scale(0.6)

        self.add(title, text)
        self.play(Create(table))
        self.wait(10)


class e6(Scene):
    def construct(self):
        title = Text("Vetor Média")
        title.shift(UP*3).scale(.6)

        text = Text("Média das linhas da matriz normalizada, mostra qual é a mais preferível", color=YELLOW)
        text.shift(UP*1.5).scale(.45)

        data = [
            ["0.0722", "0.1376", "0.4938", "0.0307", "0.2634"]
        ]

        col_labels1 = [
            Text("1.1", font_size=24),
            Text("1.2", font_size=24),
            Text("2.1", font_size=24),
            Text("2.2", font_size=24),
            Text("2.3", font_size=24)
        ]

        col_labels2 = [
            Text("1.1", font_size=24),
            Text("1.2", font_size=24),
            Text("2.1", font_size=24),
            Text("2.2", font_size=24),
            Text("2.3", font_size=24)
        ]

        # First table
        table = Table(
            data,
            col_labels=col_labels1,
            top_left_entry=Text("Subcritérios", font_size=24),
            include_outer_lines=True,
            h_buff=1.2,
            v_buff=0.3
        ).scale(0.6).shift(DOWN*0.5)

        # Arrow + text
        arrow = Arrow(UP*0.5, DOWN*0.5, buff=0).next_to(table, DOWN)
        arrow_text = Text("Convertendo para %", font_size=28).next_to(arrow, RIGHT)

        # Convert data to %
        data_percent = [
            [f"{float(x)*100:.2f}%" for x in data[0]]
        ]

        table_percent = Table(
            data_percent,
            col_labels=col_labels2,
            top_left_entry=Text("Subcritérios", font_size=24),
            include_outer_lines=True,
            h_buff=1.2,
            v_buff=0.3
        ).scale(0.6).next_to(arrow, DOWN)

        # Animate
        self.add(title, text)
        self.play(Create(table))
        self.wait(4)
        self.play(GrowArrow(arrow), Write(arrow_text))
        self.wait(3)
        self.play(Create(table_percent))
        self.wait(5)



class e7(Scene):
    def construct(self):
        title = Text("Matrizes de Comparação dos Candidatos")
        title.shift(UP*3).scale(.6)

        text = Text("Comparação entre os 5 candidatos em relação ao subcritério 1.1", color=YELLOW)
        text.shift(UP*1.5).scale(.45)

        text1 = Text("Foram feitas comparações entres os candidatos em relação a cada subcritério")
        text1.shift(UP*2.5).scale(.45)

        text2 = Text("E em seguida o processo de normalização para achar os vetores médias")
        text2.shift(UP*2).scale(.45)


        data = [
            ["1",   "3",   "1/3", "3",   "3"],
            ["1/3", "1",   "1/3", "3",   "1/3"],
            ["3",   "3",   "1",   "9",   "3"],
            ["1/3", "1/3", "1/9", "1",   "1/3"],
            ["1/3", "3",   "1/3", "3",   "1"]
        ]

        # Row labels
        row_labels = [
            Text("C1", font_size=24),
            Text("C2", font_size=24),
            Text("C3", font_size=24),
            Text("C4", font_size=24),
            Text("C5", font_size=24)
        ]

        # Column labels
        col_labels = [
            Text("C1", font_size=24),
            Text("C2", font_size=24),
            Text("C3", font_size=24),
            Text("C4", font_size=24),
            Text("C5", font_size=24)
        ]

        # Create the table
        table = Table(
            data,
            row_labels=row_labels,
            col_labels=col_labels,
            top_left_entry=Text("1.1", font_size=24),
            include_outer_lines=True,
            h_buff=1.2,
            v_buff=0.5
        ).scale(0.6)
        table.shift(DOWN*.7)

        # Mostrando na tela
        self.add(title, text, text1, text2)
        self.play(Create(table))

        self.wait(10)

class e8(Scene):
    def construct(self):
        title = Text("Matrizes Prioridade")
        title.shift(UP*3).scale(.6)

        text = Text("Formada pelos vetores médias dos candidatos entre cada subcritério", color=YELLOW)
        text.shift(UP*2.5).scale(.45)

        data = [
            ["0.2394", "0.2838", "0.2510", "0.2510", "0.1592"],
            ["0.1045", "0.0285", "0.0724", "0.0724", "0.0608"],
            ["0.4457", "0.4422", "0.3881", "0.3881", "0.4129"],
            ["0.0495", "0.1992", "0.1161", "0.1161", "0.0983"],
            ["0.1606", "0.0461", "0.1722", "0.1722", "0.2686"],
        ]

        col_labels = [
            Text("1.1", font_size=24),
            Text("1.2", font_size=24),
            Text("2.1", font_size=24),
            Text("2.2", font_size=24),
            Text("2.3", font_size=24)
        ]

        row_labels = [
            Text("C1", font_size=24),
            Text("C2", font_size=24),
            Text("C3", font_size=24),
            Text("C4", font_size=24),
            Text("C5", font_size=24),
        ]

        table = Table(
            data,
            col_labels=col_labels,
            row_labels=row_labels,
            top_left_entry=Text("*", font_size=24),
            include_outer_lines=True,
            h_buff=1.2,
            v_buff=0.5
        ).scale(0.6).shift(DOWN*0.5)

        self.add(title, text)
        self.play(Create(table))
        self.wait(7)

        self.play(FadeOut(VGroup(text, table)))
        self.wait(2)

        text1 = Text("Pesos dos candidatos", color=YELLOW)
        text1.shift(UP*2.5).scale(.45)

        data1 = [
            ["0.2303", "0.0656", "0.4063", "0.1180", "0.1796"]
        ]

        col_labels1 = [
            Text("C1", font_size=24),
            Text("C2", font_size=24),
            Text("C3", font_size=24),
            Text("C4", font_size=24),
            Text("C5", font_size=24)
        ]


        table1 = Table(
            data1,
            col_labels=col_labels1,
            top_left_entry=Text("", font_size=24),
            include_outer_lines=True,
            h_buff=1.2,
            v_buff=0.5
        ).scale(0.8).shift(DOWN*0.5)
        

        self.play(FadeIn(VGroup(text1, table1)))
        self.wait(4)
        self.play(FadeOut(VGroup(table1)))
        self.wait(2)

        text2 = Text("O candidato 3 é a melhor opção, tendo 40.63% de preferência", color=BLUE)
        text2.shift(UP*1.5).scale(.45)

        data2 = [
            ["23.03%", "6.56%", "40.63%", "11.80%", "17.96%"]
        ]

        col_labels2 = [
            Text("C1", font_size=24),
            Text("C2", font_size=24),
            Text("C3", font_size=24),
            Text("C4", font_size=24),
            Text("C5", font_size=24)
        ]


        table2 = Table(
            data2,
            col_labels=col_labels2,
            top_left_entry=Text("", font_size=24),
            include_outer_lines=True,
            h_buff=1.2,
            v_buff=0.5
        ).scale(0.8).shift(DOWN*0.5)

        self.play(FadeIn(VGroup(table2, text2)))
        self.wait(5)

# manim -ql ani.py e


