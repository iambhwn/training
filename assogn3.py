1..........................

# def a_fun():
#  	global name
# name = 'A'
# def b_fun():
#  	global name
# name = 'B'
# b_fun()
# a_fun()
# print (name)


# 2.............
# a = 10
# def f():
#  	print ('Inside f() : ', a)
# def g(): 
#  	a = 20
# print ('Inside g() : ',a)
# def h(): 
#  	global a
# a = 30
# print ('Inside h() : ',a)
# print ('global : ',a)
# f()
# print ('global : ',a)
# g()
# print ('global : ',a)
# h()
# print ('global : ',a)

# 3..................
# a_var = 10
# b_var = 15
# e_var = 25
# d_var = 100
# def a_func(a_var):
#     print("in a_func a_var =", a_var)
#     b_var = 100 + a_var
#     d_var = 2 * a_var
#     print("in a_func b_var =", b_var)
#     print("in a_func d_var =", d_var)
#     print("in a_func e_var =", e_var)
#     return b_var + 10
# c_var = a_func(b_var)
# print("a_var =", a_var)
# print("b_var =", b_var)
# print("c_var =", c_var)
# print("d_var =", d_var)

# 4.....................
# a,b,x,y = 1,15,3,4
# def fun(x, y):
#  	global a
# a = 42
# x,y = y,x
# b = 33
# b = 17
# c = 100
# print (a,b,x,y)
# fun(17,4)
# print (a,b,x,y)


# 5..........
# def f():
#  x = 42
# def g():
#  		global x
# x = 43
# print("Before calling g: ",x)
# g()
# print("After calling g: ",x)
 
# f()
# print("x in main: " ,x)

# 6.
# def outer():
#     s="Ludhiana" 
# def inner1():
#     s="punjab"
# def inner2():
#     nonlocal s
# s="Chandigarh"
# def inner3():
#     global s
# s="Haryana"
# print(s) 
# inner1() 
# print(s) 
# inner2()
# print(s) 
# inner3()
# print(s) 
# outer()
# print(s)