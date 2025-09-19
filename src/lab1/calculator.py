import re

#Функция, определяющая приоритет операций
#(2-умножение и деление,1-сложение и вычитание, 0-скобки и другие символы)

def priority(op):
    if op == "+" or op == "-":
        return 1
    if op == "*" or op == "/":
        return 2
    return 0

def operation(operators, values):
    op = operators.pop()
    second = values.pop()
    first = values.pop()
    if op == "+":
        values.append(first + second)
    elif op == "-":
        values.append(first - second)
    elif op == "*":
        values.append(first * second)
    elif op == "/":
        if second == 0:
            raise ZeroDivisionError("Деление на ноль!!")
        values.append(first / second)

def calculate(expression):
    values = []
    operators = []
    expression = expression.replace(" ","")
    tokens = re.findall(r"(\d+(\.\d*)?|\.\d+|\+|-|\*|/|\(|\))", expression)
