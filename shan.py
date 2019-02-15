from turtle import*

def one(x,y): #竖
    penup()
    setheading(90)
    goto(x,y)
    pendown()
    backward(500)

def onee(x,y): #竖
    penup()
    setheading(90)
    goto(x,y)
    pendown()
    backward(550)


def two(x,y): #撇
    penup()
    setheading(-60)
    goto(x,y)
    pendown()
    backward(100)

def twoo(x,y): #撇
    penup()
    setheading(-30)
    goto(x,y)
    pendown()
    backward(100)

def three(x,y): #横
    penup()
    setheading(0)
    goto(x,y)
    pendown()
    forward(350)

def radiuss(x,y): 
    penup()
    setheading(60)
    goto(x,y)
    pendown()
    circle(600,25)

def radiusss(x,y): 
    penup()
    setheading(-60)
    goto(x,y)
    pendown()
    circle(400,20)

def setting():          #参数设置
    pensize(10)
    hideturtle()        #使乌龟无形（隐藏）
    colormode(255)      #将其设置为1.0或255.随后 颜色三元组的r，g，b值必须在0 .. cmode范围内
    color((255,155,192),"pink")
    setup(840,500)
    speed(2)
    title("马万骁")


def main():
    setting()        
    one(-100,250)
    two(-50,220) 
    three(-40,250)  
    onee(310,250) 
    twoo(310,-300)
    radiuss(30,-100)
    radiusss(80,10)
    done()

if __name__ == '__main__':
	main()

