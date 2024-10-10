from vpython import *
ball = sphere(pos=vector(-5,0,0), radius=0.5, color=vector(1,0.7,0.7))
wallR = box(pos=vector(6,0,0), size=vector(0.2,12,12), color=color.green)
wallL=box(pos=vector(-6,0,0),size=vector(0.2,12,12),color=color.green)
wallU=box(pos=vector(0,6,0),size=vector(12,0.2,12),color=color.blue)
wallD=box(pos=vector(0,-6,0),size=vector(12,0.2,12),color=color.blue)
wallB=box(pos=vector(0,0,-6),size=vector(12,12,0.2),color=color.red)
ball.velocity = vector(25,5,-15)
deltat = 0.005
t = 0
vscale = 0.1
varr = arrow(pos=ball.pos, axis=vscale*ball.velocity, color=color.yellow,make_trail=True)
scene.autoscale = False
while True:
    rate(5000)
    varr.pos=ball.pos
    varr.axis=vscale*ball.velocity
    if ball.pos.x>wallR.pos.x:
        ball.velocity.x=-ball.velocity.x
    if ball.pos.x<wallL.pos.x:
        ball.velocity.x=-ball.velocity.x
    if ball.pos.y>wallU.pos.y:
        ball.velocity.y=-ball.velocity.y
    if ball.pos.y<wallD.pos.y:
        ball.velocity.y=-ball.velocity.y
    if ball.pos.z<wallB.pos.z:
        ball.velocity.z=-ball.velocity.z
    if ball.pos.z>-wallB.pos.z:
        ball.velocity.z=-ball.velocity.z
    ball.pos = ball.pos + ball.velocity*deltat
    t=t+deltat
