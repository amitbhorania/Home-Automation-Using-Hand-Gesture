from sklearn import tree

data = [] # training data set
labels = [] # traning label set
test = [] # test data set

with open ('testing.csv') as testf:
    row = 0 # skip the first line
    for line in testf:
        testSamples = line.strip().split(",") # trim whitespaces
        if(row >0):
            test.append([float(num) for num in testSamples]) # convert string to float
        row +=1

with open ('training.csv') as f:
    row = 0 # skip the first line
    for line in f:
        trainSamples = line.strip().split(",") # trim whitespaces
        if(row > 0):
            data.append([float(num) for num in trainSamples[:-1]])
            labels.append(trainSamples[-1])
        row +=1

clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(data, labels)

print(clf.predict(test))
