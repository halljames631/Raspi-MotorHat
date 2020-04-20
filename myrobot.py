from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import time
import Tkinter as tk 

mh = Raspi_MotorHAT(addr=0x6F)

leftFront = mh.getMotor(1)
rightFront = mh.getMotor(2)
leftRear = mh.getMotor(3)
rightRear = mh.getMotor(4)

leftFront.setSpeed(200)
rightFront.setSpeed(200)
leftRear.setSpeed(200)
rightRear.setSpeed(200)


def forward():
    leftFront.run(Raspi_MotorHAT.FORWARD)
    rightFront.run(Raspi_MotorHAT.FORWARD)
    leftRear.run(Raspi_MotorHAT.FORWARD)
    rightRear.run(Raspi_MotorHAT.FORWARD)
    

def right():
    leftFront.run(Raspi_MotorHAT.FORWARD)
    leftRear.run(Raspi_MotorHAT.FORWARD)
    
def left():
    rightFront.run(Raspi_MotorHAT.FORWARD)
    rightRear.run(Raspi_MotorHAT.FORWARD)
       
    

def reverse():
    leftFront.run(Raspi_MotorHAT.BACKWARD)
    rightFront.run(Raspi_MotorHAT.BACKWARD)
    leftRear.run(Raspi_MotorHAT.BACKWARD)
    rightRear.run(Raspi_MotorHAT.BACKWARD)

def stop():
    leftFront.run(Raspi_MotorHAT.RELEASE)
    rightFront.run(Raspi_MotorHAT.RELEASE)
    leftRear.run(Raspi_MotorHAT.RELEASE)
    rightRear.run(Raspi_MotorHAT.RELEASE)


master = tk.Tk()


a = tk.Button(master,text="forword",command=forward)
a.pack()
b = tk.Button(master,text="backup",command=reverse)
b.pack()
c = tk.Button(master,text="stop",command=stop)
c.pack()
d = tk.Button(master,text="right",command=right)
d.pack()
d = tk.Button(master,text="left",command=left)
d.pack()

master.mainloop()



