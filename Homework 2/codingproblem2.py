#Joshua Jaja ID:1543343 Coding Problem 2:

def file_xy():
    m_l ={'january': 1 ,'february':2,'march':3,'april':4,'may':5,'june':6,'july':7,'august':8,'september':9,
          'october':10,'november':11,'december':12
    }
#Part B
    with open('C:\\Users\\Joshua Jaja\\Desktop\\inputdates.txt') as f1:
        l1=f1.read().splitlines()

    i=0
    l2=[]
    l3=[]
# Part A
    for j in range(len(l1)):
        if(l1[j].find("/")==-1):
            l3.append(l1[j])
    print(l3)

    while(l3[i]!="-1"):
        s1 = ""
        n_l=l3[i].split(" ")
        if(n_l[0].lower() in m_l.keys() and n_l[1].endswith(',') and
                (int(n_l[2])>=1000 and int(n_l[2])<=2020)):
            s1+=str(m_l[n_l[0].lower()])+'/'+n_l[1][:-1]+'/'+n_l[2]+'\n'
            l2.append(s1)
        i+=1
# Part C
    f2 = open('parsedDates.txt', 'w+')
    f2.writelines(l2)
    f2.close()
file_xy()
