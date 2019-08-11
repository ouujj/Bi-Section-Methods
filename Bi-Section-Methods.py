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
diction = fucntion.count('x')
print("All diction = ",diction)

def myfucntion(x):
    return float(eval(fucntion))

                      
def sign(x):
    return math.copysign(1, x)


def plotGrap(xk):
    pa,py,pz,= [],[],[]
    plt.plot([0,b0+1], [0,0],'black')
    plt.plot([0,a0+1], [0,0],'black')
    
    for ax in range((b0-a0+1)*100):
        pa.append(a0+(ax/100))
        py.append(myfucntion(a0+(ax/100)))
        
    for z in range (len(pxk)):
        pz.append(0)
   # print("pa:",pa)
   # print("py:",py)
    plt.plot(pa, py,'green')
    plt.plot(pxk,pz,'ro')
    plt.plot(xk,0,'bo')
    plt.title('Bi-Section Methods')
    plt.show()

#main
    
if(myfucntion(a)* myfucntion(b) < 0):
#if(True):    
    print("Max Round = ",n)
    for k in range(n):
        print("\nRoudn:",k+1)
        xk = (a+b)/2
        pxk.append(xk)
        print("xk = ",xk)
        fb = myfucntion(b)
        fa = myfucntion(a)
        fx = myfucntion(xk)
        print("f(x) = ",fx)
    
        if(abs(fx) <= e):
            
            print("Find root with value <= tolerance @ ",xk)
            diction = diction - 1
            
        if(xk != 0):
            if(abs((xk1-xk)/(xk)) <= e):
                print("Find root with relative <= tolerance  @ ",xk)
                diction = diction - 1
      
        if(diction <= 0):
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
    plotGrap(0)



