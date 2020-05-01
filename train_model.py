from joblib import dump
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC

if __name__ == "__main__":
    df = pd.read_csv("iris.csv")
    y = df.loc[:, "variety"]
    X = df.drop(labels="variety", axis=1)
    le = LabelEncoder()
    le.fit(y)
    y = le.transform(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)

    print(X_train, y_train)

    clf = SVC(gamma='auto')
    clf.fit(X_train, y_train)
    print(X_test)
    y_pred = clf.predict(X_test)

    print(y_test, y_pred)

    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    dump(clf, open("model.pk", 'wb'))
    dump(le, open("le.pk", "wb"))
    print("Model Saved")

    print(clf.predict([[5.0, 3.4, 1.6, 0.4]]))
