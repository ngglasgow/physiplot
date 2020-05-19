from bokeh.io import output_notebook, show
output_notebook()
from bokeh.layouts import column
from bokeh.models import TextInput, Button, Paragraph

def modify_doc(doc):
    
    # create some widgets
    button = Button(label="Say HI")
    input = TextInput(value="Bokeh")
    output = Paragraph()

    # add a callback to a widget
    def update():
        output.text = "Hello, " + input.value
    button.on_click(update)

    # create a layout for everything
    layout = column(button, input, output)

    # add the layout to curdoc
    doc.add_root(layout)
    
# In the notebook, just pass the function that defines the app to show
# You may need to supply notebook_url, e.g notebook_url="http://localhost:8889" 
show(modify_doc, notebook_url="http://localhost:8889")