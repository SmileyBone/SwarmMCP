
import Tkinter as tk




if __name__ == "__main__":
    window = tk.Tk()
    canvas = tk.Canvas(window, width = 800, height = 800)
    canvas.pack()
    which = canvas.create_oval(drone1.position.x,drone1.position.y,drone1.position.x+10,drone1.position.y+10,fill="red", tag='redBall')

    while True:
        canvas.move('redBall', drone1.position.x - lastPos.x, drone1.position.y - lastPos.y)
        canvas.after(20)
        canvas.update()

    window.mainloop()
