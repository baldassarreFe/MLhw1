import numpy

import monkdata as m
from dtree import entropy
from dtree import averageGain


monks = {'monk1':m.monk1, 'monk2':m.monk2, 'monk3':m.monk3}
# Entropy

entropyTable = []
for key in monks:
	print key,  entropy(monks[key])


#print len([item.attribute[4] for item in m.monk1 if item.attribute[4] ==1])


# Information Gain

for key in monks:
	output = str(key)
	for attribute in m.attributes:
		output += ' ' + str(averageGain(monks[key], attribute))
	print output




