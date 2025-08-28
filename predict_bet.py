import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# 1. 데이터 준비
# 사용자가 제공한 엑셀 데이터를 pandas DataFrame으로 생성합니다.
# 실제 사용할 때는 엑셀 파일(예: game_data.xlsx)을 pd.read_excel('game_data.xlsx')로 불러오면 됩니다.

#df = pd.read_excel("soccer_data.xlsm", sheet_name="Result")
df = pd.read_excel("LightGBM_Dataset_soccer_total.xlsm", sheet_name="LaLiga")

# 2. 타겟 변수 생성 (승/무/패)
# 홈 승리: 2, 무승부: 1, 원정 승리: 0
df['target'] = np.where(df['score'] > df['conceded'], 2,
                       np.where(df['score'] == df['conceded'], 1, 0))

# 3. 특성 선택 (데이터 누수 방지!)
# 'score', 'conceded', 'diff'는 결과에 해당하므로 예측에 사용하지 않습니다.
features = ['Home', 'Away', 'Home_Form', 'Away_Form',
            'Home_Rank', 'Away_Rank', 'home_avg_goals', 'away_avg_goals']
X = df[features]
y = df['target']

# 4. 범주형 데이터 인코딩
# LightGBM은 범주형 특성을 직접 처리할 수 있지만, 여기서는 LabelEncoder를 사용하여 정수로 변환합니다.
# 팀 이름('Home', 'Away')은 모델이 이해할 수 있는 숫자 형태로 변환해야 해요.
# 더 많은 팀이 있을 경우 One-Hot Encoding보다 Label Encoding 후 categorical_feature로 지정하는 것이 효율적일 수 있습니다.
# 여기서는 간단히 LabelEncoder를 사용합니다.
le_home = LabelEncoder()
le_away = LabelEncoder()

X['Home_encoded'] = le_home.fit_transform(X['Home'])
X['Away_encoded'] = le_away.fit_transform(X['Away'])

# 이제 원본 'Home'과 'Away' 컬럼 대신 인코딩된 컬럼을 사용할 거예요.
X = X.drop(columns=['Home', 'Away'])

# 5. 데이터 분리 (훈련 세트와 테스트 세트)
# 전체 데이터의 80%를 훈련용으로, 20%를 테스트용으로 나눕니다.
# 'random_state'는 코드를 다시 실행해도 동일한 결과를 얻을 수 있게 해줘요.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
# 참고: 데이터가 매우 적으므로, stratify=y를 사용하여 각 클래스(승/무/패)의 비율을 유지합니다.

# 6. LightGBM 모델 학습
# num_class=3 (승/무/패)은 다중 클래스 분류임을 알려주고, objective='multiclass'로 목표를 설정합니다.
lgb_clf = lgb.LGBMClassifier(objective='multiclass', num_class=3, random_state=42)

# 모델 훈련!
print("LightGBM 모델 훈련 중...")
lgb_clf.fit(X_train, y_train)
print("모델 훈련 완료!")

# 7. 모델 평가
# 테스트 세트를 사용하여 예측을 수행합니다.
y_pred = lgb_clf.predict(X_test)

# 예측 정확도 확인
accuracy = accuracy_score(y_test, y_pred)
print(f"\n모델 정확도: {accuracy:.2f}")

# 더 자세한 평가 보고서
# 0: 원정 승리, 1: 무승부, 2: 홈 승리
print("\n분류 보고서:")
print(classification_report(y_test, y_pred, target_names=['원정 승리', '무승부', '홈 승리']))

# 8. 새로운 경기 예측 예시 (만약 예측하고 싶은 새로운 경기가 있다면!)
# 예를 들어, '새로운팀A'와 '새로운팀B'의 경기를 예측한다고 가정
# 이 팀들이 훈련 데이터에 없었다면 LabelEncoder에서 오류가 발생할 수 있습니다.
# 이를 방지하기 위해 'handle_unknown' 파라미터를 사용하여 알 수 없는 팀은 특정 값으로 처리하거나,
# 아니면 모델 학습 시 모든 가능한 팀을 고려하여 Label Encoding을 수행해야 합니다.
# 여기서는 예시를 위해 훈련 데이터에 있는 팀들로 가정합니다.

print("\n--- 새로운 경기 예측 ---")

# 예측할 데이터 프레임을 만듭니다.
# 예시: '가와사키'(Home), 'FC도쿄'(Away)의 가상 경기
# 가정: Home_Form:2, Away_Form:1, Home_Rank:1, Away_Rank:3, home_avg_goals:2, away_avg_goals:1
# (이 값들은 실제 예측 시 입력될 정보들을 의미합니다.)
new_game_data = {
    'Home': ['셀타'],
    'Away': ['베티스'],
    'Home_Form': [0],
    'Away_Form': [0],
    'Home_Rank': [8],
    'Away_Rank': [9],
    'home_avg_goals': [1.6],
    'away_avg_goals': [1.3]
}
new_game_df = pd.DataFrame(new_game_data)

# 예측 전에 똑같이 팀 이름을 인코딩해야 해요!
# 훈련 데이터에 fit된 LabelEncoder를 사용합니다.
try:
    new_game_df['Home_encoded'] = le_home.transform(new_game_df['Home'])
    new_game_df['Away_encoded'] = le_away.transform(new_game_df['Away'])
    
    new_game_X = new_game_df.drop(columns=['Home', 'Away'])
    
    predicted_proba = lgb_clf.predict_proba(new_game_X) # 각 결과에 대한 확률 예측
    predicted_class = lgb_clf.predict(new_game_X)       # 가장 높은 확률의 결과 클래스
    
    result_map = {0: '원정 승리', 1: '무승부', 2: '홈 승리'}
    
    print(f"가상 경기 ({new_game_data['Home'][0]} vs {new_game_data['Away'][0]}) 예측 결과:")
    print(f"  예측 클래스: {result_map[predicted_class[0]]}")
    print(f"  예측 확률: 홈 승리({predicted_proba[0][2]*100:.2f}%), 무승부({predicted_proba[0][1]*100:.2f}%), 원정 승리({predicted_proba[0][0]*100:.2f}%)")

except ValueError as e:
    print(f"오류 발생: {e}")
    print("훈련 데이터에 없는 팀은 예측할 수 없습니다. LabelEncoder가 새로운 팀 이름을 처리할 수 있도록 더 많은 팀 데이터로 재학습하거나 다른 인코딩 방법을 사용해야 합니다.")