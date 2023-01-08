from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Line, Triangle
from kivy.graphics.texture import Texture
from PIL import Image, ImageDraw
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.vertex_instructions import Rectangle



class DrawingWidget(Widget):
    def __init__(self, **kwargs):
        super(DrawingWidget, self).__init__(**kwargs)
        self.lines = []
        self.color = (1, 0, 0)  # Red
        self.size = (1000, 1000)
        self.set_background()
        self.load_image()


    def set_background(self):
        # Load the image file
        img = Image.open('background.jpg')

        # Get the size of the image
        width, height = img.size

        # Create a texture from the image
        texture = Texture.create(size=(width, height))
        texture.blit_buffer(img.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
        # fit texture in a widget size
        texture.wrap = 'repeat'
        texture.uvsize = (width / self.width, height / self.height)

        # Create a Rectangle with the texture, and set its size to the size of the DrawingWidget
        with self.canvas:
            # Calculate the x and y position of the Rectangle
            x = self.center_x - width / 2
            y = self.center_y - height / 2
            pos = (x, y)

            # Create the Rectangle with the texture, and set its position and size
            Rectangle(texture=texture, pos=pos, size=self.size)




    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud['line'] = Line(points=(touch.x, touch.y), color=self.color)
            self.lines.append(touch.ud['line'])


    def on_touch_move(self, touch):
        touch.ud['line'].points += (touch.x, touch.y)

    def save_image(self, *args):
        # Create an image with the same size as the widget
        img = Image.new('RGB', (int(self.width), int(self.height)))

        # Create a PIL draw object to draw on the image
        draw = ImageDraw.Draw(img)

        # Iterate over all lines and draw them on the image
        for line in self.lines:
            draw.line(line.points, fill=(255, 0, 0))

        # Save the image to a file
        img.save('drawing.png')
        print('Saved drawing.png')

    def load_image(self):
        # Load the saved image
        img = Image.open('drawing.png')

        # Convert the image to a texture
        texture = Texture.create(size=(img.size))
        texture.blit_buffer(img.tobytes(), colorfmt='rgb', bufferfmt='ubyte')

        # Create a triangle mesh to display the texture
        with self.canvas:
            Triangle(texture=texture, points=[0, 0, self.width, 0, self.width, self.height])

    def clear_canvas(self, *args):
        self.canvas.clear()
        self.lines = []
        self.set_background()
        

    def set_color(self, color):
        self.color = color
        print('Color set to {}'.format(color))

class MyApp(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='horizontal')

        # Create the drawing widget
        widget = DrawingWidget()

        # Create the save button
        button = Button(text='Save', size_hint=(0.1, 1))

        # Create the clear button
        button2 = Button(text='Clear', size_hint=(0.1, 1))
        button2.bind(on_press=widget.clear_canvas)

        # Create the color buttons
        red_button = Button(text='Red', size_hint=(0.1, 1))
        red_button.bind(on_press=lambda x: widget.set_color((1, 0, 0))) 


        # Bind the save_image function to the button's on_press event
        button.bind(on_press=widget.save_image)

        # Add the widgets to the layout
        layout.add_widget(widget)
        layout.add_widget(button)
        layout.add_widget(red_button)
        layout.add_widget(button2)

        # Return the root widget
        return layout


if __name__ == '__main__':
    MyApp().run()

