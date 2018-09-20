# python docu_classify.py
import matplotlib.pyplot as plt

classes = ['entertainment', 'exercise', 'family', 'food', 'people', 'pets', 'school', 'shopping', 'work']
colors = ['b','g','r','c','y','m','k','#FFA500','#8B4513']

color_index = 0
leg_list = []
for item in classes:
	infile = open(item+'_text.csv','r',encoding='utf-8')
	text_data = infile.read().split('\n')
	infile.close()
	
	length_stat = {}
	for sentence in text_data:
		sentence = sentence.split(' ')
		if str(len(sentence)) in length_stat: length_stat[str(len(sentence))] += 1
		else: length_stat[str(len(sentence))] = 1
	
	x_axis = []
	y_axis = []
	for key in length_stat:
		x_axis.append(int(key))
		y_axis.append(length_stat[key])
	
	temp_leg = plt.scatter(x_axis, y_axis, c = [colors[color_index] for i in range(len(x_axis))], s=20)
	leg_list.append(temp_leg)
	color_index += 1
	
plt.xlabel('Length of Sentences', fontsize=14)
plt.ylabel('Number of Sentences of this Length', fontsize=14)
plt.legend(leg_list, classes, loc=1, fontsize=12, title='Topics')
plt.show()