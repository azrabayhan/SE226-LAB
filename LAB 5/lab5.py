#task1
def factorialFunction(number):
    if number == 0 or number == 1:  
        return 1
    return factorialFunction(number - 1)* number

#task2

ePowerX = lambda x,n : x**n /factorialFunction(n)

def exp_x(x, n):
    sum = 0
    i = 0

    while i < n:
        sum += ePowerX(x,i)
        i += 1
    return sum    

x = input(float("enter x : "))
n = input(int("enter n: "))
    
#task3


Sn = 0
"""
    Bu fonksiyon, S_n = 1 - 1/2 + 1/3 - 1/4 + ... + (-1)^(n+1)/n
    toplamını recursive olarak hesaplıyor.
    
    Mantık:
    - Eğer n = 1 ise toplamı 1 yapıyoruz 
    - Değilse önce n-1 için toplamı hesaplıyoruz, sonra n. terimi ekliyoruz.
    - (-1)^(n+1)/n ifadesi işareti otomatik olarak doğru yapıyor.
    """
def harmonicSeriFunction(n):
 
    global Sn
    if n == 1:
        Sn += 1   
    else:
        harmonicSeriFunction(n-1)       
        Sn += (-1)**(n+1) / n            

