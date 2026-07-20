from core.predictor import StudentDropPredictor
from core.recommendation import RecommendationEngine
from core.utils import probability_to_percent


predictor = StudentDropPredictor()

student = {

    "Age at enrollment":20,
    "Gender":1,
    "Debtor":0,
    "Scholarship holder":1,
    "Tuition fees up to date":1,
    "Admission grade":140,

    "Curricular units 1st sem (approved)":6,
    "Curricular units 1st sem (grade)":15,

    "Curricular units 2nd sem (approved)":7,
    "Curricular units 2nd sem (grade)":16
}

prediction, probability = predictor.predict(student)

print("="*50)
print("Prediction :", prediction)
print("Probability :", probability_to_percent(probability), "%")
print("Risk :", RecommendationEngine.get_risk_level(probability))

print()

for item in RecommendationEngine.get_recommendation(probability):

    print("✓", item)