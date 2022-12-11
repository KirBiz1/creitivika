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
    frameRate(15)
def draw():
    global x,y1,y2,y3,y4,y5,y6
    background(192,192,192)
    rect(20+x,y1,120,60)
    ellipse(45+x,280,40,40)
    point(45+x,280)
    ellipse(110+x,280,40,40)
    point(110+x,280)
    fill(220,20,60)
    rect(150+x,y2,120,60)
    ellipse(175+x,280,40,40)
    point(175+x,280)
    ellipse(240+x,280,40,40)
    point(240+x,280)
    fill(1,50,32)
    rect(280+x,y3,120,60)
    ellipse(305+x,280,40,40)
    point(305+x,280)
    ellipse(370+x,280,40,40)
    point(370+x,280)
    fill(220,20,60)
    rect(410+x,y4,120,60)
    ellipse(435+x,280,40,40)
    point(435+x,280)
    ellipse(500+x,280,40,40)
    point(500+x,280)
    fill(220,20,60)
    rect(410+x,y5,40,40)
    fill(1,50,32)
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
    line(0,300,700,300)


    

    


    
    
