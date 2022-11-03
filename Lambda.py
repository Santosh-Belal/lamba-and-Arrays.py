print("First one ")

x=lambda a:a*5

print(x(10))

print("Second one")

b=lambda b,c:b*c

print(b(10,20))

print("Third one")

d=lambda d,e,f :d*e+f

print(d(2,10,15))

#print("Fourth One")

#def my_func(n):

 #   return lambda a:a*n

print("Fifth one ")

def my_function(z):

    return lambda a: a*z

my_double=my_function(2)

my_triple=my_function(3)

print(my_double(10))

print(my_triple(10))
