import joblib
import pandas as pd

from config import MODEL_PATH
from core.preprocessing import StudentPreprocessor


class StudentDropPredictor:

    def __init__(self):

        self.model = joblib.load(MODEL_PATH)

        self.preprocessor = StudentPreprocessor()


    def predict(self, student_dict):

        X = self.preprocessor.transform(student_dict)

        prediction = int(
            self.model.predict(X)[0]
        )

        probability = float(
            self.model.predict_proba(X)[0][1]
        )

        return prediction, probability


    def predict_dataframe(self, df):

        X = self.preprocessor.transform(
            df.to_dict("records")[0]
        )

        prediction = self.model.predict(X)

        probability = self.model.predict_proba(X)

        return prediction, probability