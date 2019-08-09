import math
import matplotlib.pyplot as plt


fucntion = input("Enter Fucntion (single value by x): ")
a=float(input("Enter a horizon:"))
a0 = int(a)
b=float(input("Enter b horizon:"))
b0 = int(b)
e=float(input("Enter tolerance:"))
n=int((b-a)/e)   
xk, xk1  = 0,0
pxk=[]


def myfucntion(x):
    return float(eval(fucntion))

                      
def sign(x):
    return math.copysign(1, x)


def plotGrap(xk):
    pa,py,pz,= [],[],[]
    plt.plot([0,b0], [0,0],'black')
    for a0 in range(b0):
        pa.append(a0)
        py.append(myfucntion(a0))
    for z in range (len(pxk)):
        pz.append(0)
    plt.plot(pa, py,'green')
    plt.plot(pxk,pz,'ro')
    plt.plot(xk,0,'bo')
    plt.title('Bi-Section Methods')
    plt.show()

#main
    
if(myfucntion(a)*myfucntion(b) < 0):
    print("Max Round = ",n)
    for k in range(n):
        print("\nRoudn:",k+1)
        xk = (a+b)/2
        pxk.append(xk)
        print("xk = ",xk)
        fb = myfucntion(b)
        fa = myfucntion(a)
        fx = myfucntion(xk)
        
    
        if(abs(fx) <= e):
            print("Find root with value <= tolerance  @ ",xk)
            
            plotGrap(xk)
            break
    
        if(abs((xk1-xk)/xk) <=  e):
            print("Find root with relative <= tolerance  @ ",xk)
           
            plotGrap(xk)
            break
        
        xk1 = xk
        if(sign(fx) != sign(fb)):
            print("chang ak+1 ")
            a = xk
     
        if(sign(fx) != sign(fa) ):
            print("chang bk+1 ")
            b = xk

else:
    print("Can not Solve it !!!!")
    plotGrap()


        
