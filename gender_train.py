# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer as Vectorizer
from sklearn.naive_bayes import BernoulliNB as Classifier
from sklearn.externals import joblib
from utils import *


vectorizer = Vectorizer(min_df=1)
classifier = Classifier()

males_train = read_lines('./data/male_train.txt')
females_train = read_lines('./data/female_train.txt')
train_set = males_train + females_train
labels = [MALE_LABEL] * len(males_train) + [FEMALE_LABEL] * len(females_train)

train_features = vectorizer.fit_transform(train_set)
classifier.fit(train_features, labels)

# save model
joblib.dump(vectorizer, './data/models/gender/vectorizer.pkl')
joblib.dump(classifier, './data/models/gender/classifier.pkl')

test_set = [u'Снегирев Роман',
            u'Ольга Лепорская',
            u'Саша Сидоров',
            u'Арнольд Шварценеггер',
            u'Женя Иванова',
            u'Вера Брежнева',
            u'Алексей Вальков',
            u'Yakov Malinov',
            u'Лука Мудищев',
            u'Пидор Мутный']

test_features = vectorizer.transform(test_set)
predictions = classifier.predict(test_features)
print predictions
