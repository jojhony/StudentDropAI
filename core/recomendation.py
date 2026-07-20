class RecommendationEngine:

    @staticmethod
    def get_risk_level(probability):

        if probability < 0.30:
            return "LOW"

        elif probability < 0.70:
            return "MEDIUM"

        return "HIGH"


    @staticmethod
    def get_recommendation(probability):

        if probability < 0.30:

            return [
                "Continue regular academic monitoring.",
                "Maintain current learning progress."
            ]

        elif probability < 0.70:

            return [
                "Schedule a meeting with the academic advisor.",
                "Monitor student performance monthly."
            ]

        return [
            "Immediate academic counselling.",
            "Review financial assistance eligibility.",
            "Assign a mentor.",
            "Weekly academic monitoring."
        ]