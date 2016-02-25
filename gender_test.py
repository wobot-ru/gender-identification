# -*- coding: utf-8 -*-
import numpy as np
from sklearn.externals import joblib
from utils import *

classifier = joblib.load('./data/models/gender/classifier.pkl')
vectorizer = joblib.load('./data/models/gender/vectorizer.pkl')

test_set = read_lines('./data/male_test.txt')
test_features = vectorizer.transform(test_set)
predictions = classifier.predict(test_features)
accuracy = np.mean(predictions == MALE_LABEL)
print 'Prediction accuracy: %f' % accuracy


