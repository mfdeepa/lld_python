from ..strategy.WritingStrategy import WritingStrategy

class DottedWriting(WritingStrategy):

    def write(self):
        print(f"Pen is writing to doted-writing style")


class RoughWriting(WritingStrategy):
    def write(self):
        print("pen is writing in Rough way")


class SmoothWriting(WritingStrategy):
    def write(self):
        print("pen is writing in Smooth way")