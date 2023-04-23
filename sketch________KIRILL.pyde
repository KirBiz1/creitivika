x = 225
x1 = 240
x2 = 255
x3 = 380 
x4 = 395
x5 = 410
#x6 =
#x7 = 
#x8 = 
def setup():
    size(600,400)
    background(249,132,229)
    frameRate(80)
def draw():
    global x,x1,x2,x3,x4,x5
    background(249,132,229)
    strokeWeight(7)
    line(0,380,600,380)
    strokeWeight(0)
    rect(150,345,35,35)
    fill(0)
    rect(163,357,10,10)
    if keyPressed==True:
        if key==CODED:
            if keyCode==UP:
                fill(255)
                background(249,132,229)
                fill(0,255,0)    
                rect(150,300,35,35)
                fill(255,0,0)
                rect(163,312,10,10)
                strokeWeight(7)
                line(0,380,600,380)
    if keyPressed==False:
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
    triangle(x,377,x1,341,x2,377)
    x = x - 1
    x1 = x1 - 1 
    x2 = x2 - 1
    triangle(x3,377,x4,341,x5,377)
    x3 = x3 - 1
    x4 = x4 - 1 
    x5 = x5 - 1
    

    

        
    


 
        

            
    
    
