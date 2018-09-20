# python LDA_v3.py

import os
import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

n_top_words = 10

def print_top_words(model, feature_names, n_top_words):
	for topic_idx, topic in enumerate(model.components_):
		message = "Topic #%d: " % topic_idx
		message += " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])
		print(message)
	print()

def judge_class(model, feature_names, n_top_words, topic_dict):
	score = {'entertainment':0, 'exercise':0, 'family':0, 'food':0, 'people':0, 'pets':0, 'school':0, 'shopping':0, 'work':0}
	for topic_idx, topic in enumerate(model.components_):
		topic_words = [feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]
		for word in topic_words:
			for key in topic_dict:
				if word in topic_dict[key]: score[key]+=1
	return max(score, key=score.get)

topic_dict = {}
filenames = os.listdir()
for filename in filenames:
	if filename.endswith('-dict.csv'):
		infile = open(filename, 'r', encoding='utf-8')
		temp_list = infile.read().split('\n')
		topic_dict[filename.replace('-dict.csv','')]=temp_list

pre_text = []
infile = csv.reader(open('data.csv','r',encoding='utf-8'))

text_data = []
for item in infile:
	text_data.append([item[0],item[4]])

outfile = open('result.csv', 'w', encoding='utf-8')
for text in text_data[1:]:
	print(text[1])
	temp_text = [text[1]]
	cv = CountVectorizer()
	tc = cv.fit_transform(temp_text)

	print('LDA process has started...')
	#lda = LatentDirichletAllocation(n_components=3, max_iter=5, learning_method='online', learning_offset=50., random_state=0)
	lda = LatentDirichletAllocation(n_components=1, max_iter=5, learning_method='online', learning_offset=50., random_state=0)
	lda.fit(tc)
	print('LDA process has ended...')
	feature_names = cv.get_feature_names()
	#print_top_words(lda, feature_names, n_top_words)
	
	outfile.write(text[0]+','+judge_class(lda, feature_names, n_top_words, topic_dict)+'\n')
outfile.close()
