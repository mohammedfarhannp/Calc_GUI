def Add(x, y):
    return x + y

def Diff(x, y):
    return x - y

def Product(x, y):
    return x * y

def Div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Zero Division Error")
        return None 
