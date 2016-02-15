import math
pi = 3.14159
def my_function(x):
    return x**2-4
def mod():
    L = [0,2,4,6,8,10]
    new = []
    l = len(new)
    a = input("which number do you want")
    for i in range (len(L)):
        new.append(L[i]+a)
        print "%d changed to %d" % (L[i], new[i+l])
##########################################
def fib():
    a = 1.0
    a2 = 1.0
    n = 2.0
    for i in range(30):
        print n
        a = n
        n=a2+n
        a2 = a
#########################################
def gra():
    x=[]
    y=[]
    for i in range(-2,2):
        x.append(i)
        y.append(2*i-1.5)
    print y
gr = 1.61803398875
#########################################
def tridf():
    for x in range(-3,3):
        for y in range(-4,4):
            z=3*x-y**2
            print "(%d,%d,%d)"%(x,y,z)
#########################################
def tridff():
    x=[]
    y=[]
    z=[]
    for i in range(-2,3):#x loop
        for j in range(-3,4):#y loop
            x.append(i)
            y.append(j)
            zval = 3*i-j**2
            z.append(zval)
    print x
    print y
    print z
#########################################
def eo():
    x = int(input("Pick a whole number."))
    if x%2 ==0:
        print 'Even'
    else:
        print 'Odd'
    print 'Done!'
#########################################
def f(x):
    if x =="A":
        return 4.0
    elif x=="A-":
        return 3.67
    elif x=="B+":
        return 3.33
    elif x=="B":
        return 3.0
    elif x=="B-":
        return 2.67
    elif x=="C+":
        return 2.33
    elif x=="C":
        return 2.0
    elif x=="C-":
        return 1.67
    elif x=="D+":
        return 1.33
    elif x=="D":
        return 1.0
    elif x=="D-":
        return 0.67
    elif x=="F":
        return 0.0
#########################################
def gpa():
    g = 0
    civ=[]
    c = 0
    math=[]
    m = 0
    lang=[]
    l = 0
    sci=[]
    s = 0
    civn = input("how many humanitities do you take?")
    for i in range(0,civn):
        civ.append(f(raw_input("whats your civ grade?")))
    mathn = input("how many maths do you take?")
    for j in range(0,mathn):
        math.append(f(raw_input("whats your math grade?")))
    langn = input("how many languages do you take?")
    for k in range(0,langn):
        lang.append(f(raw_input("whats your language grade?")))
    scin = input("how many sciences do you take?")
    for n in range(0,scin):
        sci.append(f(raw_input("whats your science grade?")))
    for ii in range(0,len(civ)):
        c = c+civ[ii]
    for jj in range(0,len(math)):
        m = m+math[jj]
    for kk in range(0,len(lang)):
        l = l+lang[kk]
    for nn in range(0,len(sci)):
        s = s+sci[nn]
    g=(c+m+l+s)/(len(civ)+len(math)+len(lang)+len(sci))
    print g
#########################################
def least(x,y,z):
    if x<y:
        if x<z:
            print "%d is least" %x
        else:
            print "%d is least" %z
    elif y<z:
        print "%d is least" %y
    else:
        print "%d is least" %z
#########################################
def lrgodd(x,y,z):  #takes the largest odd of three numbers x,y and z
    if x%2==1 and y%2==1 and z%2==1 :   ###if all are odd
        if x>y :
            if x>z:
                print "the largest odd is %d"%x #x is largest
            else:
                print "the largest odd is %d"%z #x is bigger than y and smaller than z, z is largest
        elif y>z:
            print "the largest odd is %d"%y     #if x is smaller than y and y is bigger than z
        else:
            print "the largest odd is %d"%z #if x is smaller than y and y is smaller than z
    elif x%2==1 and y%2==1 and z%2==0:  #if x and y are odd, other is even
        if x>y:
            print "the largest odd is %d"%x ##next three lines print biggest of 2
        else:
            print "the largest odd is %d"%y  
    elif x%2==1 and y%2==0 and z%2==1:  ##these are just copied and pasted and switched to where x and z are odd but y is even
        if x>z:
            print "the largest odd is %d"%x
        else:
            print "the largest odd is %d"%z
    elif x%2==0 and y%2==1 and z%2==1:  #another pasted where y and z are odd but x is even
        if y>z:
            print "the largest odd is %d"%y
        else:
            print "the largest odd is %d"%z
    elif x%2==1 and y%2==0 and z%2==0:  ##if any of the varibales are the only odd it returns they are the largest
        print "the largest odd is %d"%x
    elif x%2==0 and y%2==1 and z%2==0:
        print "the largest odd is %d"%y
    elif x%2==0 and y%2==0 and z%2==1:
        print "the largest odd is %d"%z
    elif x%2==0 and y%2==0 and z%2==0:  #if none are odd prints that
        print "None are Odd!"
    else: print "What?" #if code runs imprpoerly prints this, makes sure it covers all bases
#########################################
def lrgod(x,y,z):
    L=[]    #name sempty list "L"
    if x%2 ==1:
        L.append(x) #if x is odd put it in the list
    if y%2==1:
        L.append(y) #if y is odd put it in the list
    if z%2 ==1:
        L.append(z) #if z is odd put it in the list
    ans = max(L)    # print the biggest from the list of odds
    print ans
#########################################
def calculate(value, function):
    x = value
    return eval(function)  #defines calculate as the evaluation of a function on an input
#########################################
def summation():
    tot=[]  #defines new empty list
    str = raw_input("Whats the function? (Use x)")  #gets the function as a string
    l = input("From?")  #gets the the range of inputs
    u = input("To?")
    for i in range(l,u+1):  #for every input, appends the f(input) to the list 
        tval =calculate(i,str)
        tot.append(tval)
    t=sum(tot)  #takes the sum of the list
    print t
#########################################
def product():
    tot=[]  #defines new empty list
    t = 1
    str = raw_input("Whats the function? (Use x)")  #gets the function as a string
    l = input("From?")  #gets the range of inputs
    u = input("To?")
    for i in range(l,u+1):  #for every input appends the f(input) to the list
        tval =calculate(i,str)
        tot.append(tval)
    for j in range(0,len(tot)): #multiplies every number in the list
        t=t*tot[j]
    print t
#########################################
def factorial(num):
    i =0
    prod = 1
    while i<num:
        prod = (i+1)*prod
        i+=1
    return prod
#########################################
def nCr(n,r):
    ans = factorial(n)/(factorial(r)*factorial(n-r))
    print 
#########################################
def nPr(n,r):
    print factorial(n)/(factorial(n-r))
#########################################
def factor(num):
    i=2 #begin i at 2 because we already know that 1 is a factor
    F=[1] #f is set of factors
    while i<=(num/2):   #runs loop for every number less than or equal to the target number
        if num%i==0:    #if the target number over the input has a remainder of 0 add input to list
            F.append(i)
        i+=1
    F.append(num)   #the target is a factor of itself
    if len(F)==2:   #if only 1 and target are factors then it is prime
        print "Its prime!"
    print F
#########################################
def riemann(l,u):  ###Evaluates the summation function but uses variable n, to denote how many rectangles the graph is broken into. Evaluates the sum from lower*n to upper*n of the graph and divides each value by n
    tot=[]  #defines new empty list
    n = 1000#float(input("Number of rectangles?"))
    str = raw_input("Whats the function? (Use x)")  #gets the function as a string
    #l = input("From?")  #gets the the range of inputs
    #u = input("To?")
    for i in range(int(l*n),int(u*n+1)):  #for every input, appends the f(input) to the list 
        j = i/n
        tval=calculate(j,str)
        tval = tval/n
        tot.append(tval)
    t = round(sum(tot),2)  #takes the sum of the list
    return t
#########################################
def mid(x,y):
    return 0.5*x[-1]+0.5*y
#########################################
def bisection(a,b):
    #str = raw_input("Whats the function? (Use x)")  #gets the function as a string
    c=[]#set of midpoints
    a.append(input("From?"))#asks for interval containging 0
    b.append(input("To?"))
    m = (a+b)/2
    c.append(m)#appends the middle of the interval to the c list
    
    while round(my_function(c[-1]),4) !=0: #(calculate(c[-1],str),4) != 0:
        if (my_function(c[-1]),4)<0:#calculate(c[-1],str)<0:#if the y value is above 0
            c.append(mid(c,b)) #adds the midpoint of c and right margin to the c list
            if (my_function(c[-1]),4)>0:#calculate(c[-1],str)>0:#if the right margin has a y-value above 0
                b.append(mid(c,b)) #then move the right margin to the midpoint of c point and old right margin
        elif (my_function(c[-1]),4)>0:#(c[-1],str)>0:#same above code, but when c is above 0, using left margins
            c.append(mid(c,a))
            if (my_function(c[-1]),4)<0:#calculate(c[-1],str)<0:
                a.append(mid(c,a))
    print c[-1]
    
#########################################
def intersect():
    str = raw_input("Whats the first function? (Use x)")  #gets the function as a string
    func = raw_input("Whats the second function? (Use x)")  #gets the function as a string
    a=[]#set of left margins of interval
    b=[]#set right margins of interval
    c=[]#set of midpoints
    a.append(input("From?"))#asks for interval containging 0
    b.append(input("To?"))
    m = (a[0]+b[0])/2
    c.append(m)#appends the middle of the interval to the c list
    while round(calculate(c[-1],str),4) != round(calculate(c[-1],func),3):
        if calculate(c[-1],str)<calculate(c[-1],func):#if the y value is above y-value from evaluating second function
            c.append(mid(c,b)) #adds the midpoint of c and right margin to the c list
            if calculate(c[-1],str)>calculate(c[-1],func):#if the right margin has a y-value above y-value from second function
                b.append(mid(c,b)) #then move the right margin to the midpoint of c point and old right margin
        elif calculate(c[-1],str)>calculate(c[-1],func):#same above code, but when c is above y-value from second function, using left margins
            c.append(mid(c,a))
            if calculate(c[-1],str)<calculate(c[-1],func):
                a.append(mid(c,a))
    print c[-1]
#########################################
def der(x,str):
    return round((calculate(x+0.00001,str)-calculate(x,str))/0.00001,4)
#########################################
def extrema():
    str = raw_input("Whats the function? (Use x)")  #gets the function as a string
    a=[]#set of left margins of interval
    b=[]#set right margins of interval
    c=[]#set of midpoints
    a.append(input("From?"))#asks for interval containing 0
    b.append(input("To?"))
    m = (a[0]+b[0])/2
    c.append(m)#appends the middle of the interval to the c list
    
    while der(c[-1],str) != 0:
        if der(c[-1],str)<0:#if the dy value is above 0
            c.append(mid(c,b)) #adds the midpoint of c and right margin to the c list
            if der(c[-1],str)>0:#if the right margin has a dy-value above 0
                b.append(mid(c,b)) #then move the right margin to the midpoint of c point and old right margin
        elif der(c[-1],str)>0:#same above code, but when c is above 0, using left margins
            c.append(mid(c,a))
            if der(c[-1],str)<0:
                a.append(mid(c,a))
    print round(c[-1],4)#bisects the function that represents the derivative
#########################################
def nameflip():
    name = raw_input("Whats your name?")
    print name[::-1] #indexes the code from right to left, calling the elements of the string in reverse order
#########################################
def avg(x,y): #average of two numbers
    new = 0.5*x+0.5*y
    return new
#########################################
def max(x,y):#takes biggest of two numbers
    if x>y:
        return x
    else:
        return y
#########################################
def quad(a,b,c): #quadratic formula with real numbers
    x=[] 
    if (b**2)-(4*a*c)==0:
        x.append(-b/(2*a))
        print "the only root is %d" %x[0]
    elif (b**2)-(4*a*c)<0:
        print "no real roots"
    elif (b**2)-(4*a*c)>0:
        x.append((-b+math.sqrt((b**2)-(4*a*c)))/(2*a))
        x.append((-b-math.sqrt((b**2)-(4*a*c)))/(2*a))
        print "the roots are %d and %d" %(x[0],x[1])
def quadyint(a,b,c):
    print "the y intercept is %d" %c
def quadvert(a,b,c):
    vertx = -b/(2*a)
    verty = a*(vertx**2)+b*(vertx)+c
    print "the vertex is at (%f,%f)" %(vertx,verty)
    
#########################################
def realproj(vi,theta,t,mu,dep,w):
    vy=vi*math.sin(theta*(2*pi)/360)#y velocity in m/s
    vx = vi*math.cos(theta*(2*pi)/360)#x velocity in m/s
    n = 100 #coeffecient of accuracy
    d= 0.0
    hl=[0]
    h=0.0
    dvx=0.0
    dvy=0.0
    for i in range (0,n*t+1):
        dvx = (-mu*vx-dep*w)/n
        vx+=dvx
        d+=vx/n
    for j in range (0,n*t+1):
        dvy = (-9.8+mu*vy+dep*w)/n
        vy+=dvy
        h+=vy/n
        if h>hl[-1]:
            hl.append(h)
    print "reached a height of %f meters" %hl[-1]
    print "ended at (%f,%f)" %(round(d,3),round(h,3))
#########################################

