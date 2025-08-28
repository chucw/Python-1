import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report


# 1. 학습 데이터 불러오기 (엑셀에서 읽거나 직접 정의)
#data = pd.read_excel("soccer_data.xlsm", sheet_name="Result")  # 또는 DataFrame으로 직접 생성
data = pd.read_excel("LightGBM_Dataset_soccer_total.xlsm", sheet_name="LaLiga")

# 2. Result 열을 숫자로 변환
result_map = {'W': 1, 'D': 0, 'L': 2}
data['Result'] = data['Result'].map(result_map)

# 3. 피처와 타겟 정의
features = [
    'Home_Form', 'Away_Form'
    ,'Home_Rank', 'Away_Rank'
    ,'home_avg_goals', 'away_avg_goals'
#    ,'is_home_win_odds', 'is_draw_odds', 'is_away_win_odds'
]
X = data[features]
y = data['Result']

# 4. 모델 학습
X_train, X_val, y_train, y_val = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
model = lgb.LGBMClassifier(objective='multiclass', num_class=3)
model.fit(X_train, y_train)

y_pred = model.predict(X_val)

# 5. 예측할 경기 입력값 (본머스 vs 울버햄튼)
match_input = pd.DataFrame([{
    'Home_Form': 0
    ,'Away_Form': 0
    ,'Home_Rank': 8
    ,'Away_Rank': 9
    ,'home_avg_goals': 1.6
    ,'away_avg_goals': 1.3
#    ,'is_home_win_odds': 4.00
#    ,'is_draw_odds': 3.67
#    ,'is_away_win_odds': 1.90
}])

# 6. 예측
pred_proba = model.predict_proba(match_input)[0]
pred_class = model.predict(match_input)[0]

# 7. 결과 출력
accuracy = accuracy_score(y_val, y_pred)
print(f"\n모델 정확도: {accuracy:.2f}")

label_inverse_map = {1: 'Home Win', 0: 'Draw', 2: 'Away Win'}
print("📊 예측 결과:", label_inverse_map[pred_class])
print("🔢 확률 (홈승/무/원정승):", {
    'Home Win': round(pred_proba[1]*100, 2),
    'Draw': round(pred_proba[0]*100, 2),
    'Away Win': round(pred_proba[2]*100, 2)
})