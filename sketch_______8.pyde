x1 = 20
y1 = 200
x2 = 150
y2 = 200
x3 = 280
y3 = 200
x4 = 410
y4 = 200
x5 = 410
y5 = 160
x6 = 480
y6 = 170

x = 0
def setup():
    size(700,500)
    frameRate(20)
def draw():
    global x,y1,y2,y3,y4,y5,y6
    background(0)
    rect(20+x,y1,120,60)
    fill(1,50,32)
    rect(150+x,y2,120,60)
    fill(220,20,60)
    rect(280+x,y3,120,60)
    fill(220,20,60)
    rect(410+x,y4,120,60)
    fill(220,20,60)
    rect(410+x,y5,40,40)
    fill(220,20,60)
    rect(480+x,y6,30,30)
    fill(1,50,32)
    x = x + 1
    point(random(0,700),random(0,500))
    point(random(0,700),random(0,500))
    point(random(0,700),random(0,500))
    point(random(0,700),random(0,500))
    point(random(0,700),random(0,500))
    point(random(0,700),random(0,500))
    point(random(0,700),random(0,500))
    strokeWeight(5)
    stroke(255)
    


    
    
