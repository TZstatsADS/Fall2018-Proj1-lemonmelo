# python LDA_v3.py

import os
import csv
import time

infile = csv.reader(open('data.csv','r',encoding='utf-8'))

text_data = ''
for item in infile:
	text_data+=item[4].replace('\n',' ').replace(',','')

outfile = open('word_freq.csv', 'w', encoding='utf-8')
word_list = text_data.split(' ')
word_set = set(word_list)
print(str(len(word_set)))

time.sleep(2)
num = 1
for word in word_set:
	freq = 0
	for item in word_list:
		if item == word: freq += 1
	outfile.write(word+','+str(freq)+'\n')
	print(str(num))
	num += 1

outfile.close()
