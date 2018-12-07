import csv
import math
datatrain=[]
datatest=[]
jarak=[]
k=5
def take(elem):
	return elem[0]
with open('DataTrain_Tugas3_AI.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        datatrain.append(row)
datatrain.pop(0);
with open('DataTest_Tugas3_AI.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        datatest.append(row)
datatest.pop(0);
def pengurangan(i,j,a):
	return float(datatest[i][a])-float(datatrain[j][a])
def getjarak(i,j):
	jumlah=0
	for a in range(1,6):
		jumlah+=math.pow(pengurangan(i,j,a),2)
	return [math.sqrt(jumlah),datatrain[j][6]]
def getjum(i,b):
	return 0 if b.get(str(i))==None else b.get(str(i))
def getterdekat():
	a=[]
	c=[]
	for i in range(0,k):
		a.append(jarak[i][1])
	b={i:a.count(i) for i in a}
	for i in range(0,4):
		c.append([getjum(i,b),i])
	c.sort(key=take,reverse=True)
	return c[0][1]
def clearjarak():
	jarak.clear()
def sortjarak():
	jarak.sort(key=take)
def finishing(i):
	sortjarak()
	datatest[i][6]=getterdekat()
	clearjarak()
for i in range(0,len(datatest)):
	for j in range(0,len(datatrain)):
		jarak.append(getjarak(i,j))
	finishing(i)
with open('TebakanTugas3.csv','w',newline ='\n') as hasil:
	write = csv.writer(hasil,dialect='excel')
	for i in range(0,len(datatest)) : 
		write.writerow([datatest[i][6]])
hasil.close()