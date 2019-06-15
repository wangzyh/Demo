from numpy import *

group = random.rand(4,2)
print(group)
dataSetSize = group.shape[0]
print(dataSetSize)
diffMat = tile([0,0], (dataSetSize,1)) - group
print(diffMat)
print('-'*30)
sqDiffMat = diffMat**2
print(sqDiffMat)