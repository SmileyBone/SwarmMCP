
import drone

class mcp:
    def __init__(self):
        self.drones = []
        self.zones = [] #areas that are assigned to each drone
        self.survay = None #the main area that is subdevided into zones.

    def setSurvay(topPoint, bottomPoint):
        self.survay = (topPoint, bottomPoint)

    def addZone(topPoint, bottomPoint):
        self.zones.append((topPoint, bottomPoint))

    def addDrone(self):
        self.drones.append(drone.drone())

if __name__ == "__main__":
    import Tkinter as tk
    import random
    import time
    from state_utils import point3D

    def updateDrone(drone, deltaTime, canvas):
        tartag = drone.uid + "_target"

        lastPos = drone.position
        drone.update_state(deltaTime)
        canvas.move(drone.uid, drone.position.x - lastPos.x, drone.position.y - lastPos.y)

        if drone.distToTarget < 5:
            ltp = drone.targetPositon
            drone.set_target_pos(point3D(random.random()*750+25, random.random()*750+25))
            canvas.move(tartag, drone.get_target_pos().x - ltp.x, drone.get_target_pos().y - ltp.y)


    window = tk.Tk()
    canvas = tk.Canvas(window, width = 800, height = 800)
    canvas.pack()

    master = mcp()

    for i in range(100):
        master.addDrone()

    i = 0
    for drone in master.drones:
        drone.set_uid("drone" + str(i))
        tartag = drone.uid + "_target"

        drone.position = point3D(random.random()*750+25, random.random()*750+25)
        drone.set_target_pos(point3D(random.random()*750+25, random.random()*750+25))

        canvas.create_oval(drone.position.x-5,drone.position.y-5,drone.position.x+5,drone.position.y+5,fill="red", tag=drone.uid)
        canvas.create_oval(drone.targetPositon.x-3, drone.targetPositon.y-3, drone.targetPositon.x + 3, drone.targetPositon.y + 3, fill="blue", tag=tartag)
        i = i+1

    lastTime = time.time()
    deltaTime = 0
    while True:
        for drone in master.drones:
            updateDrone(drone, deltaTime, canvas)
        canvas.after(20)
        canvas.update()

        deltaTime = time.time() - lastTime
        lastTime = time.time()

    window.mainloop()
