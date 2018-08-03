import sys, random, argparse
import numpy as np
import math 
import turtle
from PIL import Image
from datetime import datetime
from fractions import gcd

# a class that draws a Spirograph 
class Spiro:
    #constructor
    def __init__(self, xc, yc, col, R, r, l):
    
        #create the turtle object
        self.t = turtle.Turtle()
        #set the cursor shape 
        self.t.shape('turtle')
        
        #set the step in degrees
        self.step = 5
        #set the drawing complete flag 
        self.drawingComplete = False 
        
        #set the parameters 
        self.setparams(xc, yc, col, R, r, l)
        
        #initialize the drawing 
        self.restart()
        
    #set the parameters
    def setparams(self, xc, yc, col, R, r, l):
        #the Spirograph parmeters
        self.xc = xc
        self.yc = yc
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col
        #reduce r/R to its smallest form by dividing with the GCD
        gcdVal = gcd(self.r, self.R)
        self.nRot = self.r//gcdVal
        #get ratio of radii
        self.k = r/float(R)
        #set the color
        self.t.color(*col)
        #store the current angle
        self.a = 0
        
    #restart the drawing 
    def restart(self):
        #set the flag
        self.drawingComplete = False
        #show the turtle 
        self.t.showturtle()
        #go to the first point
        self.t.up()
        R, k, l = self.R, self.k, self.l
        a = 0.0
        x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
        y = R * ((1 - k) * math.sin(a) - 1 * k * math.sin((1 - k) * a / k))
        self.t.setpos(self.xc + x, self.yc + y)
        self.t.down()
        
    #draw the whole thing
    def draw(self):
        #draw the rest of the points
        R, k, l = self.R, self.k, self.l 
        for i in range(0, 360 * self.nRot + 1, self.step):
            a = math.radians(i)
            x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
            y = R * ((1 - k) * math.sin(a) - 1 * k * math.sin((1 - k) * a / k))
            self.t.setpos(self.xc + x, self.yc + y)
        #drawing is now done so hide the turtle cursor
        self.t.hideturtle()
            
    #update by one step 
    def update(self):
        #skip the reset of the steps if done
        if self.drawingComplete:
            return
        #increment the angle
        self.a += self.step 
        #draw a step 
        R, k, l = self.R, self.k, self.l 
        #set the angle
        a = math.radians(self.a)
        x = self.R * ((1 - k) * math.cos(a) + 1 * k * math.cos((1 - k) * a / k))
        y = self.R * ((1 - k) * math.sin(a) - 1 * k * math.sin((1 - k) * a / k))
        self.t.setpos(self.xc + x, self.yc + y)
        #if drawing is complete, set the flag 
        if self.a >= 360 * self.nRot:
            self.drawingComplete = True
            #drawing is now done so hide the turrle cursor 
            self.t.hideturtle()
            
    #clear everything
    def clear(self):
        self.t.clear()
            
# a class for animating Spirographs 
class SpiroAnimator:
    #constructor
    def __init__(self, N):
        #set the timer value in milliseconds
        self.deltaT = 5
        #get the window demensions
        self.width = turtle.window_width()
        self.height = turtle.window_height()
        #create the Spiro objects
        self.spiros = []
        for i in range(N):
            #generate random parameters
            rparams = self.genRandomParams()
            #set the spiro parameters
            spiro = Spiro(*rparams)
            self.spiros.append(spiro)
        #call timer 
        self.update()
        
    #restart spiro drawing 
    def restart(self):
        for spiro in self.spiros:   
            #clear 
            spiro.clear()
            #generate random parameters 
            rparams = self.genRandomParams()
            #set the spiro parameters
            spiro.setparams(*rparams)
            #restart drawing 
            spiro.restart()
            
    #generate random parameters 
    def genRandomParams(self):
        width, height = self.width, self.height 
        R = random.randint(50, min(width, height)//2)
        r = random.randint(R // 10, 9 * R // 10)
        l = random.uniform(0.1, 0.9)
        xc = random.randint(-width // 2, width // 2)
        yc = random.randint(-height // 2, height // 2)
        col = (random.random(), random.random(), random.random())
        return (xc, yc, col, R, r, l)
        
    def update(self):
        #update all spiros
        nComplete = 0 
        for spiro in self.spiros:
            #update 
            spiro.update()
            #count completed spiros
            if spiro.drawingComplete:
                nComplete += 1
        #restart if all spiros are complete 
        if nComplete == len(self.spiros):
            self.restart()
        #call the timer
        turtle.ontimer(self.update, self.deltaT)
        
    #toggle turtle cursor on and off
    def toggleTurtle(self):
        for spiro in self.spiros:
            if spiro.t.isvisible():
                spiro.t.hideturtle()
            else:
                spiro.t.showturtle()

#save drawing as PNG files
def saveDrawing():
    #hide the turtle cursor 
    turtle.hideturtle()
    #generate unique filenames
    dateStr = (datetime.now()).strftime("%Y%b%d%H%M%S")
    fileName = 'lidongde-' + dateStr 
    print 'saving drawing to %s.eps/bmp' % fileName
    #get the tkinter canvas
    canvas = turtle.getcanvas()
    #save the drawing as a postscript image
    canvas.postscript(file = fileName + '.eps')
    #use the Pillow module to convert the postscript image file to PNG
    img = Image.open(fileName + '.eps')
    img.save(fileName + '.bmp', 'bmp')
    #show the turtle cursor
    turtle.showturtle()    

#main() function
def main():
    #use sys.argv if needed 
    print 'generating spirograph...'
    #create parser
    descStr = """This program draws Spirographs using the Turtle module.
    When run with no arguments, this program draws random Spirographhs.
    
    Terminology:
    
    R: radius of outer circle
    r: radius of inner circle
    l: ratio of hole distance to r 
    """
    parser = argparse.ArgumentParser(description = descStr)
    
    #add expected arguments
    parser.add_argument('--sparams', nargs = 3, dest = 'sparams', required = False, help = "The three arguments in sparams: R, r, l.")
    
    #parse args
    args = parser.parse_args()
    
    #set the width of the drawing window to 80 percent of the screen width 
    turtle.setup(width = 0.8)
    
    #set the cursor shape to turtle
    turtle.shape('turtle')
    
    #set the title to Spirographs!
    turtle.title("lidongde")
    
    #add the key handler to save our drawings
    turtle.onkey(saveDrawing, "s")
    
    #start listening
    turtle.listen()
    
    #hide the main turtle cursor
    turtle.hideturtle()
    
    #check for any arguments sent to --sparams and draw the Spirograph
    if args.sparams:
        params = [float(x) for x in args.sparams]
        #draw the Spirograph with the given paraments
        col = (0.0, 0.0, 0.0)
        spiro = Spiro(0, 0, col, *params)
        spiro.draw()
    else:
        #create the animator object 
        spiroAnim = SpiroAnimator(4)
        #add a key handler to toggle the turtle cursor 
        turtle.onkey(spiroAnim.toggleTurtle, "t")
        #add a key handler to restart the animation
        turtle.onkey(spiroAnim.restart, "space")
        
    #start the turtle main loop
    turtle.mainloop()
    
#call main 
if __name__ == '__main__':
    main()