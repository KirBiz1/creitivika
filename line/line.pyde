x = 0



def setup():
    size(600,400)
    frameRate(40)


    
    
def draw():
    global x
    translate(300,200)
    rotate(radians(x))
    stroke(random(255),random(255),random(255))
    strokeWeight(random(50))
    line(0,x,100,0)
    x = x + 1
