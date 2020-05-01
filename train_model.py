import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

if __name__ == "__main__":
    df = pd.read_csv("iris.csv")
    y = df.loc[:, "variety"]
    X = df.drop(labels="variety", axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)

    clf = SVC(gamma='auto')
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    pickle.dump(clf, open("model.pk", 'wb'))
    print("Model Saved")
