p=1000
n=3
i=12.5
def price(p,n,i):
    si=(p*n*i)/100
    return si
si=price(p,n,i)
print("interest",si)  
total_pay=p+si
print(total_pay) 