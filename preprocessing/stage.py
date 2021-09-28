import pandas as pd
import warnings
warnings.filterwarnings(action='ignore')



# 암 병기값 분류를 위해 TNM 병기 값 전처리 (예: 사용 안되는 컬럼값의 값들을 유사한 컬럼에 더해주기)
def Preprocess(df_TNM):
    # N0 열 추가
    df_TNM['N0'] = 0
    df_n0 = (df_TNM.N1==0) & (df_TNM.N1a==0) & (df_TNM.N1b == 0) & (df_TNM.N1c == 0) & \
    (df_TNM.N2==0) & (df_TNM.N2a==0) & (df_TNM.N2b == 0) & (df_TNM.N2c == 0) & \
    (df_TNM.N3==0) & (df_TNM.N3a==0) & (df_TNM.N3b == 0)   # 3962 명
    df_TNM['N0'][df_n0] = 1

    # T4 == 1 → T4a == 1 로 간주
    df_t4 = (df_TNM.T4 == 1)  # 2763 명
    df_TNM['T4a'][df_t4] = 1

    # N2 == 1 → N2a == 1 로 간주
    df_n2 = (df_TNM.N2 == 1)  # 2757 명
    df_TNM['N2a'][df_n2] = 1

    # N2c == 1 → N2b == 1로 간주
    df_n2c = (df_TNM.N2c == 1)  # 3034 명
    df_TNM['N2b'][df_n2c] = 1


    # T1,T1a,T1b,T1c → T1 으로 간주
    df_t1 = (df_TNM.T1==1) | (df_TNM.T1a==1) | (df_TNM.T1b==1) | (df_TNM.T1c==1)
    df_TNM['T1'][df_t1] = 1

    # T2,T2a,T2b,T2C → T2 로 간주
    df_t2 = (df_TNM.T2==1) | (df_TNM.T2a==1) | (df_TNM.T2b==1) | (df_TNM.T2C==1)
    df_TNM['T2'][df_t2] = 1

    # T3,T3a,T3b → T3 로 간주
    df_t3 = (df_TNM.T3==1) | (df_TNM.T3a==1) | (df_TNM.T3b==1)
    df_TNM['T3'][df_t3] = 1

    # N1,N1a,N1b,N1c → N1 으로 간주
    df_n1 = (df_TNM.N1==1) | (df_TNM.N1a==1) | (df_TNM.N1b==1) | (df_TNM.N1c==1)
    df_TNM['N1'][df_n1] = 1

    return df_TNM


## 암 병기값 분류: 1기 -> 2기 -> 3기 -> 4기 순
def Classify(df_TNM):
    ## 1기 분류
    df_stage_1 = ((df_TNM['T1']==1)&(df_TNM['N0']==1)) | ((df_TNM['T2']==1)&(df_TNM['N0']==1))
    df_TNM['Stage'][df_stage_1] = 1


    ## 2기 분류
    # 2.A기
    df_stage_2a = ((df_TNM['T3'] == 1)&(df_TNM['N0']==1))
    df_TNM['Stage'][df_stage_2a] = 2.3

    # 2.B기
    df_stage_2b = ((df_TNM['T4a'] == 1)&(df_TNM['N0']==1))
    df_TNM['Stage'][df_stage_2b] = 2.5

    # 2.C기
    df_stage_2c = ((df_TNM['T4b'] == 1)&(df_TNM['N0']==1))  # T4b == 1 인 경우 - 없음
    df_TNM['Stage'][df_stage_2c] = 2.7


    ## 3기 분류
    # 3.A기 
    df_stage_3a = ((df_TNM['T1']==1)&(df_TNM['N1']==1)) | ((df_TNM['T2']==1)&(df_TNM['N1']==1)) | ((df_TNM['T1']==1)&(df_TNM['N2a']==1))  
    df_TNM['Stage'][df_stage_3a] = 3.3

    # 3.B기 
    df_stage_3b = ((df_TNM['T3']==1)&(df_TNM['N1']==1)) | ((df_TNM['T4a']==1)&(df_TNM['N1']==1)) | \
    ((df_TNM['T2']==1)&(df_TNM['N2a']==1)) | ((df_TNM['T3']==1)&(df_TNM['N2a']==1)) | \
    ((df_TNM['T1']==1)&(df_TNM['N2b']==1)) | ((df_TNM['T2']==1)&(df_TNM['N2b']==1))

    df_TNM['Stage'][df_stage_3b] = 3.5

    # 3.C기 
    df_stage_3c = ((df_TNM['T4a']==1)&(df_TNM['N2a']==1)) | ((df_TNM['T3']==1)&(df_TNM['N2b']==1)) | \
    ((df_TNM['T4a']==1)&(df_TNM['N2b']==1)) | ((df_TNM['T4b']==1)&(df_TNM['N1']==1)) | \
    ((df_TNM['T4b']==1)&(df_TNM['N2a']==1)) | ((df_TNM['T4b']==1)&(df_TNM['N2b']==1))  # N2x==1 인 경우는 N2a, N2b 만 count해도 됨 (앞: N2->N2a, N2c->N2b 옮김)

    df_TNM['Stage'][df_stage_3c] = 3.7


    ## 4기 분류
    df_stage_4 = (df_TNM['M1'] == 1) | (df_TNM['M1a'] == 1) | (df_TNM['M1b'] == 1) | (df_TNM['M1c'] == 1)  # 8392 명
    df_TNM['Stage'][df_stage_4] = 4

    return df_TNM