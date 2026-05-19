# Contributing Guide

이 문서는 팀 Git 협업 규칙을 정의합니다.
모든 팀원은 아래 규칙을 따르며 작업합니다.

---

## 1. 브랜치 전략 (GitHub Flow)

* `main` 브랜치는 항상 배포 가능한 상태를 유지합니다.
* 모든 작업은 `feature/*` 브랜치에서 진행합니다.
* 작업 완료 후 Pull Request를 통해 `main`으로 병합합니다.

### 브랜치 네이밍 규칙

```
feature/<name>-<task>
```

예:

* feature/jack-contributing-guide
* feature/minjeong-conflict-practice

---

## 2. 커밋 메시지 컨벤션

### 기본 형식

```
type: subject
```

### type 종류

* feat: 새로운 기능 추가
* fix: 버그 수정
* docs: 문서 수정
* refactor: 코드 리팩토링
* test: 테스트 코드

### 좋은 예

* docs: add contributing guide
* feat: add utility function for string formatting

### 금지 예

* update
* fix
* wip
* final
* temp

이유:
변경 내용과 목적을 알 수 없어 협업 히스토리 추적이 불가능함

---

## 3. Pull Request 규칙

모든 PR은 아래 내용을 포함해야 합니다:

* What: 무엇을 변경했는지
* Why: 왜 변경했는지
* How: 어떻게 검증했는지
* 관련 Issue: Closes #번호

### PR 머지 조건

* 최소 1명 이상 리뷰 승인
* 리뷰 코멘트 반영 기록 존재

---

## 4. 코드 리뷰 규칙

* 단순 "LGTM"만 남기는 리뷰 금지
* 반드시 코드 근거 기반 코멘트 작성
* 개선 제안 또는 질문 포함

### 좋은 리뷰 예시

* 이 함수는 예외 처리 없이도 안전한가요?
* 해당 로직은 O(n)인데, 더 최적화 가능한 구조가 있을 것 같습니다.
* 변수명이 의미를 명확히 전달하지 않는 것 같습니다.

---

## 5. 충돌 발생 시 대응 흐름

1. 충돌 발생 즉시 팀원 공유
2. 해당 브랜치 기준 최신 main pull
3. 충돌 파일 직접 수정
4. 해결 후 테스트 진행
5. conflict 해결 내용을 문서화

모든 충돌 기록은 `docs/conflict-resolution.md`에 남깁니다.

---

## 6. 협업 원칙

* 모든 작업은 Issue 기반으로 진행합니다
* PR 없이 main 직접 push 금지
* 작업 단위는 작게 유지합니다
* 히스토리는 가능한 읽기 쉽게 유지합니다

---

## 7. GitHub Flow 선택 이유

* 구조가 단순하여 팀 초보자도 이해하기 쉬움
* PR 기반 리뷰 문화 형성이 용이함
* 충돌 관리 및 히스토리 추적이 명확함

결과적으로 협업 과정 자체를 학습하는 데 가장 적합한 방식입니다.
