num1 = 1
num2 = 2

if num1 < 0: 
    num1 = num1 - num2
elif num2 < 0:
    num2 = num2 - num1 
elif num1 > 0 and num2 > 0: 
    soma = num1 + num2
elif num1 < 0 and num2 < 0:
    divisao = num1/num2