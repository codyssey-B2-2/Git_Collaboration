# Conflict Resolution Log

## 충돌 기록 #1

### 참여자
- 작성자: im-jongseok
- 상대: feelosophysics

### 상황(What happened)
- main에서 docs/conflic-resoultion 파일 병합 중 충돌이 발생함

### 충돌 내용(Conflict markers)
```txt
  <<<<<<< feature/im-jongseok-conflict-resolution
  ## 충돌 기록 #TEST
  =======
  ## 충돌 기록 #137
  >>>>>>> main
```

### 해결 과정(How)
- 선택한 해결 전략: refactor 첫 충돌임으로 인덱스 #1로 최종 수정.
- feelosophysics의 문서 변경이 진행 중 im-jongseok이 main에서 pull 진행 후 수정 진행. 먼저 수정 완료한 feelosophysics가 PR 생성 후 머지 완료. 이후 im-jongseok이 PR 생성 후 머지 과정에서 충돌 발생(원인:im-jongseok이 pull 한 main과 머지 시점의 main의 내용이 다름)

### 결과(Outcome)
- refactor: 원만한 합의를 통해 의견 수렴, https://github.com/codyssey-B2-2/Git_Collaboration/pull/19, https://github.com/codyssey-B2-2/Git_Collaboration/pull/20

### 배운 점(Learnings)
- im-jongseok: 같은 문서를 작업하는 그룹에서 원활한 소통이 필요함을 느꼈다. 특히 PR 승인 주체도 관련 문서 작업자가 진행 하는 것이 바람직하다고 생각한다.
- feelosophysics: 사전에 Issue와 팀원 간 소통을 통해, 팀원의 작업 내용을 인지하는 것과 작업 단위를 잘 분배하는 것이 충돌 가능성의 폭을 줄여준다고 느꼈습니다.
