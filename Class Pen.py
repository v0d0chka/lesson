class Pen:
    def write(self):
        print("write")

class Highlighter:
    def highlight(self):
        print("Gaslighting")

class Marker(Pen, Highlighter):
    pass

my_Pen = Marker
my_Pen.write()
my_Pen.take_write()
