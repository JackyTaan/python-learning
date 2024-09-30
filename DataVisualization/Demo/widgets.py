from bokeh.io import output_file, show
from bokeh.models.widgets import TextInput, Button, Paragraph
from bokeh.layouts import layout


output_file("simple_bokeh.html")


text_input = TextInput(value="Jacky")

button = Button(lable="Generate Text")

output=Paragraph()

def update():
        output.text="Hello, " + text_input.value

button.on_click(update)

lay_out=layout([[button,text_input],[output]])

show(lay_out)
