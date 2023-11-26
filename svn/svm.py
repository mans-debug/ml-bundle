import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import seaborn as sns


def plt_line(svc_model):
    w = svc_model.coef_[0]
    b = svc_model.intercept_[0]
    x_points = np.linspace(-1, 1)
    y_points = -(w[0] / w[1]) * x_points - b / w[1]
    plt.plot(x_points, y_points, c='r')


X, y = make_classification(n_samples=2000, n_features=2,
                           n_informative=2, n_redundant=0,
                           n_classes=2)
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3, stratify=y,
                                                    random_state=32)
clf = SVC(kernel='linear', random_state=32)
clf.fit(X_train, y_train)

x = X_train[:, 0]
y = X_train[:, 1]
sns.scatterplot(x=x, y=y, hue=y_train)

plt_line(clf)
plt.show()
while True:
    print("Enter coordinates")
    input_x = int(input())
    input_y = int(input())
    x = np.append(x, [input_x])
    y = np.append(y, [input_y])
    print("Ready")
    y_train = np.append(y_train, clf.predict([[input_x, input_y]]))
    sns.scatterplot(x=x, y=y, hue=y_train)
    plt_line(clf)
    plt.show()
