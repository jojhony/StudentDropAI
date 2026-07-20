import pandas as pd
import joblib

from config import (
    SCALER_PATH,
    FEATURE_COLUMNS_PATH
)


class StudentPreprocessor:

    def __init__(self):

        self.scaler = None
        self.feature_columns = None

        try:
            self.scaler = joblib.load(SCALER_PATH)
        except:
            pass

        try:
            self.feature_columns = joblib.load(
                FEATURE_COLUMNS_PATH
            )
        except:
            pass


    def transform(self, student_dict):

        df = pd.DataFrame([student_dict])

        # One-hot encode categorical columns
        df = pd.get_dummies(df)

        # Align feature order used during training
        if self.feature_columns is not None:

            df = df.reindex(
                columns=self.feature_columns,
                fill_value=0
            )

        # Scale numeric features if a scaler is available
        if self.scaler is not None:

            df[:] = self.scaler.transform(df)

        return df