from Tkinter import *

master = Tk()
w = Canvas(master, width=200, height=100)
w.pack()
w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
w.create_rectangle(50, 25, 150, 75, fill="blue")
import pyglet

window = pyglet.window.Window(resizable=True)

@window.event
def on_draw():
    window.clear()
    pyglet.gl.glColor4f(1.0,0,0,1.0)
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (10, 15, 30, 35))
    )

pyglet.app.run()