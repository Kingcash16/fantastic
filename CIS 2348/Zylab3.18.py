#Joshua Jaja ID:1543343
import math

p_color = {
'green':23,
'blue':25,
'red':35
}
w_h = int(input("Enter wall height (feet): \n"))
w_w = int(input("Enter wall width (feet):\n"))
w_area = w_w*w_h
g_coverage = 350
g=w_area/g_coverage
print("wall area: "+str(w_area) +"sq feet")
print("Paint needed: "+"{:.2f}".format(g)+"gallons")
c=math.ceil(g)
print("Cans needed: "+str(c)+" can(s)")
color=input("Choose a color to paint the wall:")
cost=0
for i in p_color.keys():
    if i == color.lower():
     cost = c*p_color[i]
if(cost == 0):
 print("Wrong color selected. Color not available.")
else:
 print ("Cost of purchasing red paint: $"+str(cost))




