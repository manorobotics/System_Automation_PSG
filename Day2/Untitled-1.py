
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

df = pd.read_csv("day2_sample.csv")

df = df.drop_duplicates()

x = df[["temperature", "pressure", "vibration", "rpm", "current"]]
y = df["state"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y
)

m = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    class_weight="balanced"
)

m.fit(x_train, y_train)

p = m.predict(x_test)

print("Accuracy:", accuracy_score(y_test, p))
print(classification_report(y_test, p, zero_division=0))

joblib.dump(m, "machine_state_model.joblib")

print("Model saved successfully")

t = pd.DataFrame([{
    "temperature": 70.0,
    "pressure": 5.0,
    "vibration": 2.0,
    "rpm": 1800,
    "current": 12.0
}])

print("Predicted state:", m.predict(t)[0])