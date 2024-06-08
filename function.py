""""
def my_function(*h):
    print("the first children is",h[0])
    print(type(h))
          
my_function("f","g","k")
"""
#
"""

def c(**n):
    print(type(n))
    return "the first name is:", n["fn"]

d = c(fn="k")
print(d)
##
"""
"""
def v(*f):
    return ["the corona positive is:", f[0], f[1], f[2], f[3]]

d = v("sumi:", 90, "ahnaf:", 40)
print(d)
"""

                #problem 
"""
def b(*m):
    result = ' '.join(m)
    return result

c = b("p", "l")
print(c)
#
def b(*m):
    result = []
    for i in m:
        result.append(i)
    return result

c = b("p", "l")
print(c)
"""
"""
def v(msg1,*msg):  
    print(msg1)
    print(msg)
v("o","l","lp")


def c(*x):
    return 5*x
v=c(5,4)
print(v,end=" ")


a="global a"
def outer():
    #c="outer a"
    def inner():
        #a="inner"
        print(a)
    inner()
    print(a)
outer()

i=0
while (i<4):
    i+=1
    print("outer of the loop:",i)
    j=1
    while j<=5:
        j+=1
        print("inside of tnhe loop:",j)
print("rest of the code")

count = 0
if (count < 3):
    print ('The count is:', count)
    count = count + 1
print ("Good bye!")

x = 10  # Number of terms to generate
a = 0
b = 1

print(a)  # Print the first term
print(b)  # Print the second term

for i in range(2, x):
    c = a + b
    a = b
    b = c
    print(c)
"""
count=1
def printer(name):
    global count
    if count<=10:
        print(name)
        count+=1
        printer(name)
printer("kajol")