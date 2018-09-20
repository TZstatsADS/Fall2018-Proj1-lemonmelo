# python docu_classify.py
import csv

classes = ['entertainment', 'exercise', 'family', 'food', 'people', 'pets', 'school', 'shopping', 'work']

infile = csv.reader(open('data.csv','r',encoding='utf-8'))

raw_text_dict = {}
for item in infile:
	raw_text_dict[item[0]]=item[4]

for item in classes:
	result = csv.reader(open('result.csv','r',encoding='utf-8'))
	print(item)
	outfile = open(item+'_text.csv', 'w', encoding='utf-8')
	for res in result:
		if res[1].strip() == item:
			outfile.write(raw_text_dict[res[0]]+'\n')
			print(res[0])
	outfile.close()