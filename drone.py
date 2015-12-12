"""the drone class represents each of the drones
in the swarm. The class provides a way to track the
state of each drone, as well as provides interface
methods for the mcp to command each drone. The mcp
then reads the state of the drone class to access the
state to update the ui."""

from state_utils import point3D

"""for now the drone class always tries to move to the target"""
class drone:
    def __init__(self):
        #drone manuver limits
        self.maxVelocity = 100 #m/s
        self.maxAccel = 1000

        #current state
        self.position = point3D(0,0,0)
        self.velocity = point3D()
        self.acceleration = point3D()
        self.distToTarget = 0
        self.uid = None

        #externaly set targets
        self.targetPositon = point3D()

        #internally set targets to reach targets
        #note that we are using a velocity controller which will always try to
        #move to the target position.
        self.commandVelocity = point3D()

    def set_uid(self, string):
        self.uid = string

    def set_target_pos(self, target):
        self.targetPositon = target

    def get_target_pos(self):
        return self.targetPositon

    #this is a very basic velocity controller
    def set_command_velocity(self):
        if self.position != self.targetPositon:
            self.commandVelocity = self.targetPositon - self.position

    #this is where the limits of the system are imposed.
    def clampState(self):
        magAccel = self.acceleration.magnitude()
        magVel = self.velocity.magnitude()
        if magAccel > self.maxAccel:
            self.acceleration = self.acceleration.scale(self.maxAccel / magAccel)
        if magVel > self.maxVelocity:
            self.velocity = self.velocity.scale(self.maxVelocity / magVel)

    def update_state(self, deltaTime):
        self.set_command_velocity()
        self.position = self.position + self.velocity.scale(deltaTime)
        self.velocity = self.velocity + self.acceleration.scale(deltaTime)

        if self.velocity != self.commandVelocity:
            self.acceleration = (self.commandVelocity - self.velocity)
        self.clampState()

        self.distToTarget = (self.position - self.targetPositon).magnitude()

    def tick(self, deltaTime):
        self.update_state(deltaTime)

if __name__ == "__main__":
    import time
    import Tkinter as tk
    import random

    random.seed()

    #then we run some tests.
    drone1 = drone()
    drone1.set_target_pos(point3D(100,100,0))
    lastTime = time.time()

    window = tk.Tk()
    canvas = tk.Canvas(window, width = 800, height = 800)
    canvas.pack()
    canvas.create_oval(drone1.position.x,drone1.position.y,drone1.position.x+10,drone1.position.y+10,fill="red", tag='drone')
    canvas.create_oval(drone1.get_target_pos().x, drone1.get_target_pos().y, drone1.get_target_pos().x + 5, drone1.get_target_pos().y + 5, fill="blue", tag='target')

    lastPos = drone1.position
    while True:
        if drone1.distToTarget < 10:
            print "moving target"
            ltp = drone1.get_target_pos()
            drone1.set_target_pos(point3D(random.random()*750+25, random.random()*750+25))
            canvas.move('target', drone1.get_target_pos().x - ltp.x, drone1.get_target_pos().y - ltp.y)

        canvas.move('drone', drone1.position.x - lastPos.x, drone1.position.y - lastPos.y)
        canvas.after(20)
        canvas.update()
        lastPos = drone1.position

        deltaTime = time.time() - lastTime
        drone1.tick(deltaTime)
        #print drone1.acceleration
        lastTime = time.time()

    window.mainloop()
