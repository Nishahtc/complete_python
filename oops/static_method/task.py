class Bank:
         bank_name="Punjab"
         rate_of_interest=12.25
         @staticmethod
         def simple_interest(p,n,r) :
                 return p*n*r/100
         
principle=float(input("enter principle num:"))
year=int(input("enter year:"))
intres=Bank.simple_interest(principle,year,Bank.rate_of_interest)
print(intres)
    
