print('function ra vared konid: ')
s = input() #daryaft moadele mored nazar
if s.startswith('"') and s.endswith('"'):
    s = s[1:-1];

def tabeh(x):
    res=eval(s);
    return res


print('avalin paramter x1:  ')
x1= int(input())#daryaft hadse aval
print('dovomin parameter x2:  ')
x2= int(input())#daryaft hadse dovom
print('daryaft khata:  ')
acc=float(input())#daryaft khata

while (tabeh(x1)*tabeh(x2)>0): #dar in halghe ta zamani ke hads ha shart lazem baraye ravesh false position ra nadashte bashan gereftan maghadir tekrar mishavad
    print('maghadir shart lazem ra nadaread,dobare talash konid')
    print('meghar jadid x1:  ')
    x1=int(input()) #daryaft mojadad x1
    print('meghdar jadid x2:  ')
    x2=int(input()) #daryaft mojadad x2

    print('meghdar tabeh dar x1 :',tabeh(x1))
    print('meghdar tabeh dar x2 :',tabeh(x2))
    res = tabeh(x1)*tabeh(x2);
    if res>0 :
         print('zarb meghadir f(x1) * f(x2) >0 ast va barabare ',res,' pas dobare talash konid')
    else:
         print('zarb meghadir f(x1) * f(x2) <0 ast va barabare ',res,' pas hale va bayad berim marhale bad! :))')


while (abs(x2-x1)>acc): #dar in halghe ta zamani ke hads ha az khataha kamtar bashad be noghte rishe nazdik mishavim
    
    x3=x1 - (((x1-x2)/(tabeh(x1)-tabeh(x2)))*tabeh(x1)) #shart false postion baraye nazdik shodan be rishe ke ravesh takmil shodeye bisection ast
    if(tabeh(x1)*tabeh(x2)<0): #har bar shart check mishavad ta meghdar rishe bedast amade ba kodam adad jabe ja shavad
     x2=x3
    else:
     x1=x3
    print(x3)
    
print('javab mishe:',x3); #az loop biroon amadeh va reshe ra chap mikonim
