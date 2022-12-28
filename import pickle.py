import pickle
students=[['Jhon','501',20,92.5],['kohli','502',21,95.5],['Ganga','503',20,90.5],['Gayathri','504',20,82.5],['Krishna','505',20,96.5]]
fst=open("students.dat","wb")
for student in students:
    pickle.dump(student,fst)
fst.close()
fst=open("students.dat",'rb')
try:
    while(True):
        print(data)
        data=pickle.load(fst)
except:
    print("Bye")