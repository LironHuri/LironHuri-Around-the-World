import pyautogui
from sympy import symbols, solve


def background_resolution():
    width,height=pyautogui.size()
    return width,height


def object_resolution(img_width,img_height):
    width,height=pyautogui.size()
    x=symbols("x")
    expr1=(width/x)-(img_width)
    expr2=(height/x)-(img_height)
    sol1=solve(expr1)
    sol2=solve(expr2)

    for i in sol1:
        sol1=round(width/i)
    for i in sol2:
        sol2=round(height/i)
    return sol1,sol2



def main():
    print("classes & functions is ON")
    print(f"working from {__name__}")


if "__main__"==__name__:
    main()
