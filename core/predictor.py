import pandas as pd
import joblib
import os


class StudentDropPredictor:

    def __init__(
        self,
        model_path="models/tuned_binary_ensemble.pkl",
        scaler_path="models/scaler.pkl"
    ):

        self.model = joblib.load(model_path)

        if os.path.exists(scaler_path):
            self.scaler = joblib.load(
                scaler_path
            )
        else:
            self.scaler = None


    def preprocess(self, student_data):

        """
        Convert input dictionary
        into model-ready dataframe
        """

        df = pd.DataFrame(
            [student_data]
        )


        # Apply scaler if available
        if self.scaler:

            numerical_columns = df.columns

            df[numerical_columns] = (
                self.scaler.transform(df)
            )


        return df



    def predict(self, student_data):

        """
        Main prediction function
        """

        X = self.preprocess(
            student_data
        )


        prediction = (
            self.model.predict(X)[0]
        )


        probability = (
            self.model
            .predict_proba(X)[0][1]
        )


        risk = self.get_risk_level(
            probability
        )


        return {

            "prediction": int(prediction),

            "probability": round(
                probability*100,
                2
            ),

            "risk": risk
        }



    def get_risk_level(
        self,
        probability
    ):


        if probability < 0.3:

            return "LOW"


        elif probability < 0.7:

            return "MEDIUM"


        else:

            return "HIGH"