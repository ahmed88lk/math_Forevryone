from manimlib import *

class OpeningManimExample(Scene):
    def construct(self):
        text = Text("Hello, ManimGL!").scale(2)
        self.play(Write(text))
        self.wait(2)
    