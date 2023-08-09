# DACON: 월간 데이콘 이미지 기반 질의 응답 AI 경진대회

<img alt="Html" src ="https://img.shields.io/badge/dacon Final rank-Top 10%25-lightblue?style=for-the-badge"/>

#### 이미지 기반 질의응답 AI 모델 개발 (23.07.10 - 23.08.07) - 길다영, 김준용

##### 📊 [PUBLIC] 9/102 (상위 10%) 점수: 0.56089
##### 📊 [PRIVATE] 9/102 (상위 10%) 점수: 0.56666

<br><br>

### 공유된 코드 사용
- DACON 코드 공유 커뮤니티에서 공유된 코드 사용하여 파라미터를 바꿔 실험함. <br>
  - *[청소 - (public 0.47928) 모델, 코드 공유](https://dacon.io/competitions/official/236118/codeshare/8490?page=1&dtype=recent)*
 

<br>

### ./shell_scripts/run_train.sh 수정

```
model_name_or_path="microsoft/git-large-r-coco"
--per_device_train_batch_size 100 \
--per_device_eval_batch_size 100 \
```

<br> 

### baseline

- 대회에서 주어진 baseline 실행 시 최대 Public Score: 0.38928 이었음.
- baseline 내에서 다음 하이퍼파라미터들을 바꿈.
```
self.effi = models.efficientnet_v2_l(pretrained=True)
self.bart = BartModel.from_pretrained('facebook/bart-base')
epochs=6
batch_size=16
```

<br>

### 아쉬운 점
- 멀티모달 분야에 경험이 없어 다양한 코드를 실험해보지 못함.
  


<br><br>


<b>출처 |</b> [DACON - 월간 데이콘 이미지 기반 질의 응답 AI 경진대회](https://dacon.io/competitions/official/236118/overview/description) <br>
