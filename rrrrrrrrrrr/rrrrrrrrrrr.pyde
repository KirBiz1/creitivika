x = 0
y = 0




def setup():
    size(400,400)
    frameRate(20)

    
    
def draw():
    global x,y
    background(0)
    fill(random(250),random(255),random(255))
    ellipse(x,y,random(70),random(70))
    x=x+1
    y=y+1
    
    



    

     
