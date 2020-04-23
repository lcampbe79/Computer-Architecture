# #:20 regarding branchtables

# def funct1(): #
#     print('funct1')

# def funct2():
#     print('funct2')

# def funct3():
#     print('funct3')

# def funct4():
#     print('funct3')

# def call_funct(n):
#     """
#     if n == 1:
#         funct1()
#     elif n == 2:
#         funct2()
#     elif n == 3:
#         funct3()
#     elif n == 4:
#         funct4()
#     """
#     branchtable = {
#         1: funct1,
#         2: funct2,
#         3: funct3,
#         4: funct4
#     }

#     #branch_table[n]()

#     f = branch_table[n]
#     f(a)
# call_funct(1)

# with arguements
def funct1(a): 
    print('funct1', a)

def funct2(a):
    print('funct2', a)

def funct3(a):
    print('funct3', a)

def funct4(a):
    print('funct3', a)

def call_funct(n, a):
    """
    if n == 1:
        funct1()
    elif n == 2:
        funct2()
    elif n == 3:
        funct3()
    elif n == 4:
        funct4()
    """
    branch_table = {
        1: funct1,
        2: funct2,
        3: funct3,
        4: funct4
    }

    #branch_table[n]()

    f = branch_table[n]
    f(a)

call_funct(1, "hi")
call_funct(2, "me")