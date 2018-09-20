# python word_cloud.py
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv

infile = csv.reader(open('data.csv','r',encoding='utf-8'))
text_data = ''
for item in infile:
	text_data+=item[4].replace('\n',' ').replace(',','')

word_cloud = WordCloud().generate(text_data)

plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
plt.show()