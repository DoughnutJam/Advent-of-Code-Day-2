f=open("Input.txt","r")

lines = f.readlines()
count=0
for line in lines:
    split1 = line.split()
    split2=list(map(int,split1[0].split('-')))
    split1[0]=list(range(split2[0],split2[1]+1))
    split1[1]=split1[1].replace(':','')

    if split1[2].count(split1[1]) in split1[0]:
           count+=1
print(count)
