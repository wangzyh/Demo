import sklearn
import csv

# from sklearn import datasets
from sklearn.feature_extraction import DictVectorizer
# from sklearn import preprocessing
# from sklearn import tree
# from sklearn.externals.six import StringIO


allElectronicsData = open(r'F:\Demo\Demo\DeepLearning\AllElectronics.csv', 'rt')
reader = csv.reader(allElectronicsData)
headers = next(reader)

print(headers)
