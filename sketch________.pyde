
 
def setup(): 
  size(640, 360)
  background(102)


def draw(): 

  variableEllipse(mouseX, mouseY, pmouseX, pmouseY)





def variableEllipse( x,  y,  px,  py):
  speed = abs(x-px) + abs(y-py);
  fill(speed,200,speed)
  rect(x, y, speed, speed)


  





  




  
