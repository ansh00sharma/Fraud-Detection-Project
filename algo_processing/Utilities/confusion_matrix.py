
def ConfusionMatrix(classifier, X_test, Y_test):

# Calculating Test Set Value.
        y_pred = classifier.predict(X_test)

# Making Confusion Matrix.
        from sklearn.metrics import confusion_matrix
        cm = confusion_matrix(Y_test, y_pred)

        mt_cm = [cm]
        return mt_cm