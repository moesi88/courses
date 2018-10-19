def sqrt(x):
    '''compute square roots using the method of heron of Alexandria.

    Args:
        x: the number for which the square root is to be computed.

    returns: 
        the square root of x .
    '''
    guess = x 
    i = 0
    while guess * guess != x and i < 20:
        guess =(guess + x / guess ) / 2.0
        i +=1
    return guess

def main ():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print("this is never printed.")
    except ZeroDivisionError:
        print("connot compute square root of a negative number.")

    print("program execution normally here.")        


if __name__ == '__main__':
    main()
