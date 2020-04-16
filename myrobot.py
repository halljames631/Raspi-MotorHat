from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

mh = Raspi_MotorHAT(addr=0x6F)

leftFront = mh.getMotor(1)
rightFront = mh.getMotor(2)

leftFront.setSpeed(200)
rightFront.setSpeed(200)

leftFront.run(Raspi_MotorHAT.FORWARD)
rightFront.run(Raspi_MotorHAT.FORWARD)