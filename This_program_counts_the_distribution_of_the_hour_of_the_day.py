Tlist = list()
Tdict = dict()

with open (input("please input the name of the file: ")) as fname:
    for check in fname:
        Tlist = check.split()
        if len(Tlist)> 3 and check.startswith('From'):
            address = Tlist[5]
            hour,minutes,secs = address.split(':')

            if hour not in Tdict:
                Tdict[hour] = 1
            else:
                Tdict[hour] += 1
   
    lst = list()
    for key,value in (Tdict.items()):
        lst.append((key,value))
    lst.sort()
 


    for keys,values in lst:
        print (keys, values)

        
