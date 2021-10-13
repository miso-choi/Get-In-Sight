## Get-In-Sight 📈  
2021 암 빅데이터 활용 인공지능 아이디어 경진대회

## 1. Topic  
### 대장암 병기 예측 모델 개발
### -조직학적 진단 및 건강정보 기반으로


## 2. Overview
환자의 조직학적 진단코드와 건강 정보를 이용하여 암 병기값을 예측합니다.  
모델 학습을 위한 데이터를 구축하기 위해 EDA를 통해 암 병기값과 상관관계가 있는 데이터를 선별하였습니다. 예측 모델로 회귀 모델을 선정하여 암 병기값을 1기, 2기, 3기, 4기로 분류하는 것에 그치지 않고, 소수값까지 예측할 수 있도록 하였습니다.  
본 프로젝트를 통해 현 인공지능 모델의 정확도를 높이는 데에 기여하려 합니다.


## 3. EDA
가설을 세운 뒤 검증하며 데이터를 파악하였습니다. ([대장암 데이터 EDA](https://github.com/miso-choi/Get-In-Sight/blob/master/EDA/Colorectal_main.ipynb))
* 가설1 - 조직학적 진단 코드값 중 1(1:예)의 개수가 많을수록 사망 비율이 높고 생존일수가 짧을 것이
다.
* 가설2 - 조직학적 진단 코드값 중 1(1: 예)의 개수가 많을수록 암 병기값이 높을 것이다.
* 가설3 - 음주와 흡연을 할수록 사망 비율이 높고 생존일수가 짧을 것이다.
* 가설4 - T,N,M병기 조합으로부터 계산된 암 병기의 값(1~4)이 클수록 사망인 경우가 많을 것이고, 암 
진단 후 생존일수가 짧을 것이다.

## 4. 방법론
암 병기 값 예측 시 소수 값까지 예측하기 위해 회귀 모델을 사용하였습니다.


