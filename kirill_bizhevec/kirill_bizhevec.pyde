# add_library("sound")
x1 = 220
x2 = 420
x3 = 620
x4 = 820
x5 = 1020
x6 = 0
x7 = 700
x8 = 500
y = 380
y1 = 368
ssize = 20
# sf = SoundFile(this,"sound.mp3")
def setup():
    size(600,400)
    background(249,200,255)
    frameRate(60)
    # sf.play()
def draw():
    global x1,x2,x3,x4,x5,x6,x7,x8,y,ssize,y1,sf
    background(100,200,255)
    strokeWeight(7)
    stroke(0)
    line(0,380,600,380)
    strokeWeight(0)
    fill(255,0,0)
    rect(150,y1,35,35)
    fill(0,255,0)
    rect(163,y,10,10)
    if keyPressed:
        if key==CODED:
            if keyCode==UP:
                y = y - 100
                y1 = y1 - 100
            if y < 282:
                y = 282
            if y1 < 270:
                y1 = 270
    if not keyPressed:
        y = y + 2 
        y1 = y1 + 2
        if y > 357:
            y = 357
        if y1 > 345:
            y1 = 345     
    strokeWeight(0)
    fill(0)
    triangle(x1, 377, x1 + ssize/2, 352, x1 + ssize, 377)
    x1 = x1 - 2.7
    triangle(x2, 377, x2 + ssize/2, 352, x2 + ssize, 377)
    x2 = x2 - 2.7
    triangle(x3, 377, x3 + ssize/2, 352, x3 + ssize, 377)
    x3 = x3 - 2.7
    triangle(x4, 377, x4 + ssize/2, 352, x4 + ssize, 377)
    x4 = x4 - 2.7 
    triangle(x5, 377, x5 + ssize/2, 352, x5 + ssize, 377)
    x5 = x5 - 2.7 
    if x1 < 0:
        x1 = random(600,4000)
    if x2 < 0:
        x2 = random(600,4000)
    if x3 < 0:
        x3 = random(600,4000)
    if x4 < 0:
        x4 = random(600,4000)
    if x5 < 0:
        x5 = random(600,4000)
    stroke(random(0,255),random(0,255),random(0,255))
    strokeWeight(random(0,10))
    point(random(x6,x7),random(x6,x8))
    point(random(x6,x7),random(x6,x8))
    point(random(x6,x7),random(x6,x8))
    point(random(x6,x7),random(x6,x8))
    point(random(x6,x7),random(x6,x8))
    point(random(x6,x7),random(x6,x8))
    point(random(x6,x7),random(x6,x8))
    strokeWeight(0)
    rect(random(x6,x7),random(x6,x8),10,10)
    rect(random(x6,x7),random(x6,x8),10,10)
    rect(random(x6,x7),random(x6,x8),10,10)
    rect(random(x6,x7),random(x6,x8),10,10)
    rect(random(x6,x7),random(x6,x8),10,10)
    rect(random(x6,x7),random(x6,x8),10,10)
    rect(random(x6,x7),random(x6,x8),10,10)
    rect(random(x6,x7),random(x6,x8),10,10)
