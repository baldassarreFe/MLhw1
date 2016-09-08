import numpy

import monkdata as m
from dtree import entropy
from dtree import averageGain
from dtree import bestAttribute
from dtree import select
#from dtree import 


monks = {'monk1':m.monk1, 'monk2':m.monk2, 'monk3':m.monk3}
# Entropy

entropyTable = []
for key in monks:
	entropyTable.append([key, entropy(monks[key])])

print entropyTable
#print len([item.attribute[4] for item in m.monk1 if item.attribute[4] ==1])


# Information Gain

infoGainTable = []
for key in monks:
	gains = []
	for a in m.attributes:
		gains.append(averageGain(monks[key], a))
	infoGainTable.append([key, dict(zip(m.attributes, gains))])

print infoGainTable

# best attribute for monk1 is A5, monk2 is A5, monk3 is A2


for key in monks:
	print key, bestAttribute(monks[key], m.attributes)




class Split:
    "Represenation of data splits"
    def __init__(self):
        self.attribute = None
        self.subsets = {}

split1 = Split()
split2 = Split() 

split1.attribute = bestAttribute(monks['monk1'], m.attributes)
print split1.attribute

for v in split1.attribute.values:
	split1.subsets[v] = select(monks['monk1'], split1.attribute, v)
	print split1.attribute, v, len(split1.subsets[v])


for value in split1.subsets:
	split2.attribute = bestAttribute(split1.subsets[value], [a for a in m.attributes if a!=split1.attribute])
	for v in split2.attribute.values:
		split2.subsets[v] = select(split1.subsets[value], split2.attribute, v)
		print split1.attribute, value, '-->', split2.attribute, v, len(split2.subsets[v])





