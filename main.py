MAX_AREA=7 # потому что в рюзаке, ингалятор занял 1 ячейка, и у Тома 2x4 ячейк
STUFFDICT={'в':(3,25),
           'п':(2,15),
           'б':(2,15),
           'а':(2,20),
           'н':(1,15),
           'т':(3,20),
           'о':(1,25),
           'ф':(1,15),
           'д':(1,10),
           'к':(2,20),
           'р':(2,20)}
necessary_stuff={'Ингалятор':('и',1,5)}
AREA=[STUFFDICT[key][0] for key in STUFFDICT.keys()]
VALUE=[STUFFDICT[key][1] for key in STUFFDICT.keys()]
number_stuff=len(STUFFDICT)

def build_table(area,value):
    number_value=len(value)
    table=[[0 for a in range(MAX_AREA+1)]for i in range (number_value+1)]
    for i in range (number_value+1):
        for a in range (MAX_AREA+1):
            if a==0 or i==0: table[i][a]=0
            elif a>=area[i-1]:
                table[i][a]=max(value[i-1]+table[i-1][a-area[i-1]],table[i-1][a])
            else:
                table[i][a]=table[i-1][a]
    return table

table=build_table(AREA,VALUE)
max_value=table[number_stuff][MAX_AREA]

def build_list_stuff(table):
    list_stuff=[]
    max=max_value
    area_1=MAX_AREA
    for i in range (number_stuff,0,-1):
        if max==0:break
        elif max==table[i-1][area_1]: continue
        else:
            max-=VALUE[i-1]
            area_1-=AREA[i-1]
            list_stuff.append((AREA[i-1],VALUE[i-1]))
    table_stuff=[]
    for search in list_stuff:
        for key, value in STUFFDICT.items():
            if search==value:
               if [key] in table_stuff:
                continue
               else: 
                    for i in range(value[0]):#value[1]==area
                        table_stuff.append([key])
                    break
    table_stuff.append(['и'])
    return table_stuff

stuff=build_list_stuff(table)

def count_sum(stuff):
    sum=max_value+20 #20 это исходный 
    for i in STUFFDICT.keys():
        if [i] in stuff:
            continue
        else:
            sum-=STUFFDICT[i][1]
    return sum

for i in range (MAX_AREA+1):
    if i in range(int((MAX_AREA+1)/2)):
       print(stuff[i], end=',')
       if i == (MAX_AREA+1)/2-1: print(stuff[i])
    else:
        print(stuff[i],end=',')
        if i==MAX_AREA: print(stuff[i])
        
print(f'Итоговые очки выживания: {count_sum(stuff)}')




    
