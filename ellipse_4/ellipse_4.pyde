x = 0
y = 0
x1 = 0
y1 = 0
x2 = 0
y2 = 0
x3 = 0
y3 = 0

def setup():
    size(800,600)
    background(0)
    frameRate(50)

def draw():
    background(0)
    translate(400,300)
    global x,x1,x2,x3,y,y1,y2,y3
    fill(random(255),random(255),random(255))
    ellipse(x,y,70,70)
    ellipse(x1,y1,70,70)
    ellipse(x2,y2,70,70)
    ellipse(x3,y3,70,70)
    y = y + 1
    y1 = y1 - 1
    x = x + 1
    x1 = x1 - 1
    x2 = x2 - 1
    y2 = y2 + 1
    x3 = x3 + 1
    y3 = y3 - 1
    
