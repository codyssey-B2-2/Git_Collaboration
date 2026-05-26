# Troubleshooting Log

## 시나리오: amend
### 참여자
- feelosophysics

### 상황
- 커밋 메시지가 컨벤션(CONTRIBUTING 규칙)에 맞지 않았고, 작업 내용을 명료하게 반영하지 않았음.

### 시도한 명령/절차
1. `git commit -m 'troubleshooting.md'`
2. 커밋 메시지에 작업이 명료하게 드러나지 않음을 인지.
3. `git commit --amend -m 'docs: troubleshooting.md 생성, trouble_amend 시나리오 작성'`

### 결과
- 새로운 커밋을 추가로 만들지 않고, 기존의 잘못된 커밋 메시지를 성공적으로 변경함. `git log --oneline --graph`로 전후 변경됨 확인함.
- 주의할 점: 이미 Push되어 원격 저장소에 올라간 커밋에 이 명령을 쓰면, 로컬과 원격의 히스토리가 불일치하게 됨.

### 왜 이 방법을 선택했는가(Why)
- 단순히 커밋 메시지를 수정한 커밋을 남기는 것보다, 하나의 완성된 의미를 가진 커밋으로 관리하는 것이 팀의 가독성을 높인다고 판단함.

---
---
---

## 시나리오: reset
### 참여자
- feelosophysics

### 상황
- 이미 커밋을 했는데, 추가 작업이 더 필요해서 커밋 자체를 취소하고 싶음.

### 시도한 명령/절차
1. `git commit --amend -m 'docs: troubleshooting.md 생성, trouble_amend 시나리오 작성'`
2. 커밋을 하긴 했는데, 아직 커밋할 단계가 아니었음. 아직 내용이 부족하여 커밋을 취소하고 다시 작업하기로 결정.
3. `git reset --soft HEAD~1`

### 결과
- `git status` 확인 결과, 커밋은 사라졌지만 내가 작성하던 파일의 내용은 삭제되지 않고 **'Staging Area(초록색 상태)'**에 그대로 남아있음. 덕분에 이어서 작업을 진행할 수 있게 됨.
- 주의할 점: **`--hard` 옵션을 쓰면 작업 중이던 코드까지 모두 날아가므로, 변경 사항을 유지하고 싶을 때는 반드시 `--soft`를 사용해야 함.**

### 왜 이 방법을 선택했는가(Why)
- 작업 중인 내용을 잃지 않으면서도(soft 옵션), 불완전한 상태의 커밋 기록이 히스토리에 남지 않도록 '실행 취소'를 하기 위해 선택함.

---
---
---

## 시나리오: stash
### 참여자
- VectorSophie

### 상황
- 작업 중이던 파일이 있었지만, 다른 브랜치로 이동해야 하는 상황이 발생함.
- 아직 작업 내용이 완성되지 않아 commit 하기 애매했고, 작업 내용을 유지한 채 잠시 보관할 필요가 있었음.

### 시도한 명령/절차
1. git stash
2. git checkout main
3. 다른 작업 수행 후 다시 원래 브랜치로 복귀
4. git stash pop

### 결과
- git stash 실행 후 working tree가 깨끗한 상태로 변경되어 안전하게 브랜치를 이동할 수 있었음.
- git stash pop 실행 후 이전에 작업하던 내용이 정상적으로 복구됨.
- 덕분에 불완전한 작업 내용을 commit 하지 않고도 작업 흐름을 유지할 수 있었음.
- 주의할 점: stash pop 과정에서도 충돌(conflict)이 발생할 수 있으므로, 브랜치 상태를 확인한 뒤 사용하는 것이 안전함.

### 왜 이 방법을 선택했는가(Why)
- 아직 완성되지 않은 작업 내용을 commit 기록으로 남기고 싶지 않았음.
- 작업 내용을 잃지 않으면서도 안전하게 브랜치를 이동하기 위해 stash를 사용함.
- 임시 저장 후 다시 복구할 수 있어 협업 중 빠른 작업 전환에 적합하다고 판단함.

---
---
---

## 시나리오: revert
### 참여자
- im-jongseok

### 상황
- 이미 커밋하고 push까지 완료했지만, 해당 커밋의 변경 사항을 되돌리고 싶음.
- 단, 커밋 기록을 삭제하지 않고 복구한 이력도 남기고 싶음.

### 시도한 명령/절차
1. `tmp/revert_test` 파일 생성 후 `git add`, `git commit`, `git push` 진행
2. 직전 커밋의 변경 사항을 되돌리기 위해 `git revert HEAD` 실행
3. revert 커밋 메시지를 저장하여 복구 커밋 작성
4. 변경 사항을 반대로 적용한 새 커밋이 생성되어 복구 완료

### 결과
- 기존 커밋 기록은 유지된 상태로, 해당 커밋의 변경 사항을 되돌리는 새 커밋이 작성됨.
- 덕분에 원격 저장소에서도 복구 이력을 확인할 수 있고, 커밋 이전과 동일한 상태로 작업을 이어갈 수 있음.
- 주의할 점: 직전 커밋이 아닌 더 이전 커밋을 revert하는 경우, 해당 커밋 이후의 작업 내용과 **충돌**이 발생해 수동 해결이 필요할 수 있음.

### 왜 이 방법을 선택했는가(Why)
- 작업 이력과 복구 이력을 모두 커밋 히스토리에 남길 수 있기 때문.

## 보너스 과제: git rebase -i 히스토리 정리

### 참여자

* VectorSophie

---

### 상황

README 작업 과정에서 여러 개의 작은 수정 커밋이 생성되었다.

초기 커밋 히스토리:

```txt
a87f841 feat: actually use shield badge
1207a7b feat: fill up readme with recent workflow, tech and such
582391b feat: fill up readme with lively architectural decisions
```

커밋 수가 많고 변경 내용이 분산되어 있어, 하나의 의미 있는 작업 단위로 정리할 필요가 있었다.

---

### 시도한 명령 / 절차

1. 최근 커밋 확인

```bash
git log --oneline
```

2. 최근 3개 커밋 interactive rebase 실행

```bash
git rebase -i HEAD~3
```

3. rebase 편집기에서 squash를 사용하여 커밋 통합

예시:

```txt
pick 582391b feat: fill up readme with lively architectural decisions
squash 1207a7b feat: fill up readme with recent workflow, tech and such
squash a87f841 feat: actually use shield badge
```

4. 최종 커밋 메시지 정리 후 저장

5. rebase 이후 변경된 commit hash를 원격 브랜치에 반영

```bash
git push origin feature/VectorSophie/fill-readme --force-with-lease
```

---

### 결과

rebase 이후 여러 개의 작은 수정 커밋이 하나의 정리된 커밋으로 통합되었다.

정리 후 히스토리:

```txt
08209d7 feat: fill up readme with lively architectural decisions
```

덕분에 commit history 가독성이 향상되었고, 하나의 작업 목적이 명확하게 드러나게 되었다.

---

### 주의할 점

* rebase는 기존 commit hash를 변경하므로 force push가 필요하다.
* 공유 브랜치에서 협의 없이 rebase를 수행하면 충돌이나 작업 손실 위험이 존재한다.
* force push 대신 `--force-with-lease` 사용이 더 안전하다.

---

### 왜 이 방법을 선택했는가 (Why)

작은 수정 단위 커밋들을 하나의 의미 있는 작업 흐름으로 정리하기 위해 interactive rebase를 사용했다.

이를 통해:

* commit history를 읽기 쉽게 만들고
* 리뷰 및 유지보수 효율을 높이며
* 불필요하게 세분화된 수정 기록을 정리할 수 있었다.
