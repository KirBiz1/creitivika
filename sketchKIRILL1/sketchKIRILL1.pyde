x1 = 240
x2 = 300
x3 = 380 
ssize = 40
y = 312
x0 = 0
y0 = 0
def setup():
    size(600,400)
    background(249,132,229)
    frameRate(80)
def draw():
    (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
    (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
    (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)
    global x,x1,x2,x3,x4,x5,x6,x7,x8,y,ssize
    background(249,132,229)
    strokeWeight(7)
    line(0,380,600,380)
    strokeWeight(0)
    rect(150,345,35,35)
    fill(0)
    rect(163,357,10,10)
    if keyPressed:
        if key==CODED:
            if keyCode==UP:
                fill(255)
                background(249,132,229)
                fill(0,255,0)    
                rect(150,300,35,35)
                fill(255,0,0)
                rect(163,y,10,10)
                strokeWeight(7)
                line(0,380,600,380)
    if not keyPressed:
        fill(255)
        background(249,132,229)
        fill(0,255,0)
        rect(150,345,35,35)
        fill(255,0,0)
        rect(163,357,10,10)
        strokeWeight(7)
        line(0,380,600,380)
    strokeWeight(0)
    fill(0)
    triangle(x1, 377, x1 + ssize/2, 341,  x1 + ssize, 377)
    x1 = x1 - 1 
    triangle(x2,377, x2 + ssize/2, 341, x2 + ssize, 377)
    x2 = x2 - 1
    triangle(x3, 377, x3 + ssize/2, 341, x3 + ssize, 377)
    x3 = x3 - 1    
    if x1 < 0:
        x1 = random(600,800)
    if x2 < 0:
        x2 = random(600,800)
    if x3 < 0:
        x3 = random(600,800)


        

    
        
    
        
        

    

        
    


 
        

            
    
    
