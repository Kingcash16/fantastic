# Joshua Jaja ID:1543343 Zylab 5.19
m = """Davy's auto shop services
Oil change $35
Tire Rotation $19
Car wash $7
Car wax $12"""
print(m)

d1 = {"Oil change":35,"Tire rotation":19,"Car wash":7,"Car wax":12,"-":"No service"}
print("\nselect first service: \n",end="")
s1 = input()
print("\nselect second service: \n",end="")
s2 = input()

print("Davy's auto shop invoice")
if s1!= '-' and s2!='-':
    print("service 1: "+s1+", $"+ str(d1[s1]))
    print("service 2: "+s1+", $"+ str(d1[s2]))
    Total = d1[s1]+d1[s2]
elif s1=="-":
    print("service1:"+"No service")
    print("Service 1:"+s1+",$"+ str(d1[s1]))
    Total = d1[s1]
else:
    print("service 1:"+s1+", $" +str(d1[s1]))
    print("service 2: "+"no service")
    Total = d1[s1]
print("\nTotal:$"+str(Total))



