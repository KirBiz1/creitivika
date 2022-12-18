def setup():
    size(600,400)
    background(0)
    frameRate(10)
    
    
def draw():
    stroke(random(255),random(255),random(255))
    strokeWeight(random(10))
    line(300,200,random(600),random(400))
