# python topic_word_cloud.py
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv

classes = ['entertainment', 'exercise', 'family', 'food', 'people', 'pets', 'school', 'shopping', 'work']

for item in classes:
	infile = open(item+'_text.csv','r',encoding='utf-8')
	text_data = infile.read()
	infile.close()

	word_cloud = WordCloud().generate(text_data)

	plt.imshow(word_cloud, interpolation='bilinear')
	plt.axis("off")
	plt.show()