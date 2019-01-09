#!/usr/bin/env python

# import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm, rcParams

## Gather Data
max_iterate = 10
bin = []
part2 = []
part1 = []

authors = []
commitCount = []
insertions = []
deletions = []

authors2 = []
line_count = []
changes = []

print('Reading File...')
file = open('./result.txt','r')
k = 0
bin.append(file.readline())
while (bin[k][0:6] != 'Author' and k<max_iterate):
	k = k+1
	bin.append(file.readline())

part1.append(file.readline())
k = 0
while(part1[k] != '\n' and k<max_iterate):
    part1.append(file.readline())
    k = k + 1
part1.remove('\n')
bin = []
k = 0
bin.append(file.readline())
while (bin[k][0:6] != 'Author' and k<max_iterate):
	k = k+1
	bin.append(file.readline())


part2.append(file.readline())
k = 0
while(part2[k] != '' and k<max_iterate):
	part2.append(file.readline())
	k = k + 1
file.close()
print('File Reading Done !')
part2.remove('')
for e in part1:
	i=0;
	k=0;
	while(k != 1):
		if e[i] == ' ' :
			k += 1
		i +=1
	authors.append(e[0:i-1])
	commitCount.append(e[30:34])
	insertions.append(e[43:50])
	deletions.append(e[58:64])
	changes.append(e[74:79])
for e in part2:
	i=0;
	k=0;
	while(k != 1):
		if e[i] == ' ' :
			k += 1
		i +=1
	authors2.append(e[0:i-1])
	line_count.append(e[28:31])

## Analyse DATA :
# Convert commitCount string elements into int :
changes = [float(i) for i in changes]
commitCount = [int(i) for i in commitCount]
insertions = [int(i) for i in insertions]
deletions = [int(i) for i in deletions]
line_count = [int(i) for i in line_count]


x = 0
for i in range(1, line_count.index(max(line_count))+1):
	x = x + line_count[i]
angle_line_count = float(x + max(line_count)/4)/float(sum(line_count))*360
x = 0
max_index_change = 0
for i in range(len(changes)):
	if(changes[max_index_change] < changes[i]):
		max_index_change = i
for i in range(1, max_index_change+1):
	x = x + line_count[i]
# print('curent=', angle_line_count)
angle_changes = float(x)
# print("angle_changes=")
# print(angle_changes)
ind = range(1, len(authors)+1)
color_tab = ['#59eb50','#fe8e00', '#00cc99', 'purple', '#af8eae', '#ef1056', '#3c42fc','#059b74', '#cc6600', '#cc0066','#993300' ,'b','c','y','r','g']
width = 0.8
adjust = width*0.75

## Make Graph :
plt.close()
fig, axarr = plt.subplots(2, 2, figsize=(12, 12), facecolor='w')
fig.canvas.set_window_title('StatiGit - Gitinspector')

axarr[0,0].set_title('% of total changes :',fontsize=16)
axarr[0,0].pie(changes, labels=authors, autopct='%1.1f%%', shadow=True,
									 radius=0.9, startangle=0, colors=color_tab)

axarr[0,1].set_title('Number of rows in current revision :', fontsize=16)
axarr[0,1].pie(line_count, labels=authors2, autopct='%1.1f%%', shadow=True,
				   radius=0.9, startangle=90+angle_line_count, colors=color_tab)

axarr[1,0].set_title('Number of commit', fontsize=18)
bars = axarr[1,0].bar(ind,  commitCount, width, align='center', color=color_tab)
axarr[1,0].set_xticks(ind)
axarr[1,0].set_xticklabels(authors, fontsize=14, horizontalalignment='center',
															rotation='vertical')
axarr[1,0].set_yticks([])
# Set Text in middle in bars :
max_height = 0
for rect in bars:
	if (max_height < rect.get_height()) :
		max_height = rect.get_height()
for rect in bars:
	height = rect.get_height()
	if(height > max_height*0.15):
		axarr[1,0].text(rect.get_x() + rect.get_width()/2., 0.5*height, '%d' % int(height), ha='center', va='center', fontsize=18)
	else :
		axarr[1,0].text(rect.get_x() + rect.get_width()/2., 0.1*max_height + 0.4*height, '%d' % int(height), ha='center', va='center', fontsize=18)

axarr[1,1].set_title('Number of insertions (green)\nand deletions (red)', fontsize=16)
p1 = axarr[1,1].bar(ind, insertions, width, align='center', color='g')
p2 = axarr[1,1].bar(ind, deletions, width, align='center', color='r', bottom=insertions)
axarr[1,1].set_xticks(ind)
axarr[1,1].set_xticklabels(authors, fontsize=14, horizontalalignment='center', rotation='vertical')
axarr[1,1].set_yticks([])

# Set Text in middle in bars :
max_height = 0
for rect in p2 :
	if (max_height < rect.get_height()) :
		max_height = rect.get_height()

for rect in p1:
	height = rect.get_height()
	if(height > max_height*0.1):
		axarr[1,1].text(rect.get_x() + rect.get_width()/2. , 0.5*height,
			'%d' % int(height), ha='center', va='center', fontsize=18)
	else :
		axarr[1,1].text(rect.get_x() + rect.get_width()/2. , 0.15*max_height,
			'%d' % int(height), ha='center', va='center', fontsize=18, color='g')

for rect in p2:
	height = rect.get_height()
	if(height > max_height*0.1):
		axarr[1,1].text(rect.get_x()+rect.get_width()/2. , rect.get_y()+0.5*height,
	 				'%d' % int(height), ha='center', va='center', fontsize=18)
	else :
		axarr[1,1].text(rect.get_x() + rect.get_width()/2. , 0.3*max_height,
			'%d' % int(height), ha='center', va='center', fontsize=18, color='r')

plt.show()
