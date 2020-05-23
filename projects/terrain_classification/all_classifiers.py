import matplotlib.pyplot as plt

from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()

ada_clf = AdaBoostClassifier()
ada_clf.fit(features_train, labels_train)
ada_pred = ada_clf.predict(features_test)
ada_accuracy = accuracy_score(labels_test, ada_pred)
print(f"The accuracy of AdaBoostClassifier is : {ada_accuracy}")

knn_clf = KNeighborsClassifier()
knn_clf.fit(features_train, labels_train)
knn_pred = knn_clf.predict(features_test)
knn_accuracy = accuracy_score(labels_test, knn_pred)
print(f"The accuracy of KNeighborsClassifier is : {knn_accuracy}")

rf_clf = RandomForestClassifier()
rf_clf.fit(features_train, labels_train)
rf_pred = rf_clf.predict(features_test)
rf_accuracy = accuracy_score(labels_test, rf_pred)
print(f"The accuracy of RandomForestClassifier is : {rf_accuracy}")


# the training data (features_train, labels_train) have both "fast" and "slow"
# points mixed together--separate them so we can give them different colors
# in the scatterplot and identify them visually

grade_fast = [
    features_train[ii][0]
    for ii in range(0, len(features_train))
    if labels_train[ii] == 0
]
bumpy_fast = [
    features_train[ii][1]
    for ii in range(0, len(features_train))
    if labels_train[ii] == 0
]
grade_slow = [
    features_train[ii][0]
    for ii in range(0, len(features_train))
    if labels_train[ii] == 1
]
bumpy_slow = [
    features_train[ii][1]
    for ii in range(0, len(features_train))
    if labels_train[ii] == 1
]


# initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color="b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color="r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


# visualization code (prettyPicture) to show you the decision boundary

try:
    prettyPicture(ada_clf, features_test, labels_test)
except NameError:
    pass

# The default accuracies without any parameter tuning
# The accuracy of AdaBoostClassifier is : 0.924
# The accuracy of KNeighborsClassifier is : 0.92
# The accuracy of RandomForestClassifier is : 0.916