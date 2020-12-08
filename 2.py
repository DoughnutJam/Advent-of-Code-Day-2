f=open("Input.txt","r")

lines = f.readlines()
count=0
for line in lines:
    split1 = line.split()
    split2=list(map(int,split1[0].split('-',1)))
    split1[1]=split1[1].replace(":",'')
    letter=split1[1]
    string=split1[2]
    minimum=split2[0]
    maximum=split2[1]
    string2=list(string)
    
    try:
        first = string[minimum-1]
        second = string[maximum-1]
        if first == letter and second == letter:
                ''
        elif  first != letter and second != letter:
                ''
        else:
                count += 1
    except IndexError:
        pass

print(count)    

