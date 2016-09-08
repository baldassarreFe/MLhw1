import numpy

import monkdata as m

from dtree import *
# from drawtree import drawTree

monks = {'monk1':m.monk1, 'monk2':m.monk2, 'monk3':m.monk3}
monktests = {'monk1':m.monk1test, 'monk2':m.monk2test, 'monk3':m.monk3test}
# Entropy

entropyTable = {}
for key in monks:
	entropyTable[key] = entropy(monks[key])

print "Entropy table"
for key in sorted(entropyTable):
	print key, '\t', entropyTable[key]
#print len([item.attribute[4] for item in m.monk1 if item.attribute[4] ==1])


# Information Gain

infoGainTable = {}
for key in sorted(monks):
	gains = []
	for a in m.attributes:
		gains.append(averageGain(monks[key], a))
	infoGainTable[key] = dict(zip(m.attributes, gains))

print "Information gain table"
line = ""
for a in m.attributes:
	line += '\t' + a.name
print line

for key in sorted(infoGainTable):
	line = key
	for a in sorted(infoGainTable[key]):
		line += '\t' + "{0:.5f}".format(infoGainTable[key][a])
	print line

# best attribute for monk1 is A5, monk2 is A5, monk3 is A2
print "best attributes for first split:"
for key in sorted(monks):
	print key, bestAttribute(monks[key], m.attributes)


# 2 levels tree for monk1

class Split:
    "Represenation of data splits"
    def __init__(self):
        self.attribute = None
        self.subsets = {}

split1 = Split()
split2 = Split()

split1.attribute = bestAttribute(monks['monk1'], m.attributes)
print "Best attribute for split 1: ", split1.attribute

for v in split1.attribute.values:
	split1.subsets[v] = select(monks['monk1'], split1.attribute, v)
	print split1.attribute, '('+`v`+')', '#' + `len(split1.subsets[v])`


for value in split1.subsets:
	split2.attribute = bestAttribute(split1.subsets[value], [a for a in m.attributes if a!=split1.attribute])
	print "Best attribute for split 2:", split2.attribute
	for v in split2.attribute.values:
		split2.subsets[v] = select(split1.subsets[value], split2.attribute, v)
		print split1.attribute,  '('+`value`+')', '-->', split2.attribute,  '('+`v`+')', '#' + `len(split2.subsets[v])`, '-->', mostCommon(split2.subsets[v])

# 2 levels tree for monk1 using buildTree
tree =  buildTree(monks['monk1'], m.attributes, 2)
print "tree", tree
print "depth", tree.depth()
# drawTree(tree)

# full decision trees for all monks
print "Full decision trees for all monks, learning from all the learning data"
print "Accuracy for training set and testing set:"
for key in sorted(monks):
	tree = buildTree(monks[key], m.attributes)
	# print tree
	print key, check(tree, monks[key]), check(tree, monktests[key])

# training and pruning

print "Full and pruned decision trees for all monks, learning from 0.6 of all the learning data"
print "Accuracy for training set and testing set"
for key in sorted(monks):
	training, validation = partition(monks[key], 0.6)
	tree = buildTree(training, m.attributes)
	prunedTree = prune(tree, validation)

	print key,"before pruning", check(tree, monks[key]), check(tree, monktests[key])
	print key," after pruning", check(prunedTree, monks[key]), check(prunedTree, monktests[key])
