## Get-In-Sight 📈  
2021 암 빅데이터 활용 인공지능 아이디어 경진대회

### 1. Topic  
#### 대장암 병기 예측 모델 개발
#### - 조직학적 진단 및 건강정보 기반으로


### 2. Overview
환자의 조직학적 진단코드와 건강 정보를 이용하여 암 병기값을 예측합니다.  
모델 학습을 위한 데이터를 구축하기 위해 EDA를 통해 암 병기값과 상관관계가 있는 데이터를 선별하였습니다. 예측 모델로 회귀 모델을 선정하여 암 병기값을 1기, 2기, 3기, 4기로 분류하는 것에 그치지 않고, 소수값까지 예측할 수 있도록 하였습니다.  
본 프로젝트를 통해 현 인공지능 모델의 정확도를 높이는 데에 기여하려 합니다.


### 3. EDA
가설을 세운 뒤 검증하며 데이터를 파악하였습니다. ([대장암 데이터 EDA](https://github.com/miso-choi/Get-In-Sight/blob/master/EDA/Colorectal_main.ipynb))

### 4. ML Model

- [DecisionTreeRegressor](https://github.com/miso-choi/Get-In-Sight/blob/master/model/Regressor_dt_rf_xgb.ipynb)
- [RandomForestRegressor](https://github.com/miso-choi/Get-In-Sight/blob/master/model/Regressor_dt_rf_xgb.ipynb)
- [XGBRegressor](https://github.com/miso-choi/Get-In-Sight/blob/master/model/Regressor_dt_rf_xgb.ipynb)
- [SVR](https://github.com/miso-choi/Get-In-Sight/blob/master/model/Regressor_svr.ipynb)  
  
➡ 위 4가지 모델의 예측결과를 가중평균하여 반환
  - [VotingRegressor](https://github.com/miso-choi/Get-In-Sight/blob/master/model/Ensemble.ipynb)  




***** 

### Contributors
|  [곽규나](https://github.com/Gyunakwak)  |  [최미소](https://github.com/miso-choi)  |  [하유빈](https://github.com/youbin01)  |
| ---- | ---- | ---- |
| <img src="https://user-images.githubusercontent.com/78155086/140711387-409d8ea7-92d7-4cd6-8c1b-431fb622886e.png" width="120px" height="120px"> | <img src="https://user-images.githubusercontent.com/78155086/140712068-0b9f67ba-d7cd-4855-84ab-b2b4c331fec2.jpeg" width="120px" height="120px"> | <img src="https://user-images.githubusercontent.com/78155086/140712252-37fab956-f609-436e-a23c-dab81d7d0d3d.png" width="120px" height="120px"> |

