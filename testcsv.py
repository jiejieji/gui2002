

import csv

def writetocsv():
	with open('data.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file)
		fw.writerow(data)




data = ['Apple',20]
writetocsv(data)



