# Undoing Things('되돌리기')

## 1. 파일 내용을 수정 전으로 되돌리기
* Unmodifying a Modified File
  * Modified 파일 되돌리기

### git restore
* git restore <파일 이름>의 형식을 사용
* git의 추적이 되고 있는==버전관리가 되고 있는 파일만 되돌리기 가능

1. 이미 버전 관리가 되고 있는 test.md 파일을 변경 후 저장(save)
```bash
# test.md
Hello
World <- "World"라는 새로운 내용 추가
-------------------------------------
이후 저장
```

2. test.md는 modified 상태
```bash
$ git status
On branch master
Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git restore <file>..." to discard changes in working directory)
modified: test.md
no changes added to commit (use "git add" and/or "git commit -a")
```

3. git restore를 통해 수정 전으로 되돌림
```bash
$ git restore test.md
```
```txt
# test.md
Hello
-------------------------------------
World가 삭제 되면서, 수정 전으로 되돌아감
```

### 중요!
  * 원래 파일로 덮어썼기 때문에 수정한 내용은 전부 사라짐
  * 한 번 git restore를 통해 수정을 취소하면, 해당 내용을 복원할 수 없음

## 2. 파일 상태를 Unstage로 되돌리기
* Unstaging a Staged File
* Staging Area와 Working Directory 사이를 넘나드는 방법
* git add를 통해서 파일을 Staging Area에 올렸을 경우, 다시 Unstage로 내리는 방법 2가지

### git rm --cached
1. 새폴더에서 git 초기화 후 진행 test.md 파일을 생성하고 git add를 진행
```bash
$ touch test.md
```

```bash
$ git add test.md
```
```bash
$ git status
On branch master
No commits yet
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
    new file: test.md
```

2. Staging Area에 올라간 test.md를 다시 내리기(unstage)
```bash
$ git rm --cached test.md
rm 'test.md'
```
```bash
$ git status
On branch master
No commits yet
Untracked files:
(use "git add <file>..." to include in what will be committed)
test.md
nothing added to commit but untracked files present (use "git add" to track)

```

### git restore --staged
* 상황 전 사전 준비
```bash
$ git add .
$ git commit -m "first commit"
```
1. test.md의 내용을 변경하고 git add를 진행
```bash
# test.md 파일 변경 후
$ git add test.md
$ git status
On branch master
Changes to be committed:
(use "git restore --staged <file>..." to unstage)
modified: test.md
```
2. Staging Area에 올라간 test.md를 다시 내리기(unstage)
```bash
$ git restore --staged test.md
```

```bash
$ git status
On branch master
Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git restore <file>..." to discard changes in working directory)
modified: test.md
no changes added to commit (use "git add" and/or "git commit -a")
```

### 중요!
  * Unstage로 되돌리는 명령어가 다른 이유? == 사용처가 다름
    * git rm --cached <file>
      * 기존에 커밋이 없는 경우
      * 'to unstage and remove paths only from the staging area'
    * git restore --staged <file>
      * 기존에 커밋이 존재하는 경우
      * 'the contents are restored from HEAD'

## 3. 바로 직전 완료한 커밋 수정하기
### git commit --amend
* 해당 명령어는 상황에 따라 2가지 기능을 가짐
  * 커밋 메시지만 수정하기 : 마지막으로 커밋하고 나서 수정한 것이 없을 때(커밋하자마자 바로 명령어를 실행한 경우)
  * 이전 커밋 덮어쓰기 : Staging Area에 새로 올라온 내용이 있을 때

#### 커밋 메시지만 수정하는 경우
1. A 기능을 완성하고 커밋
```bash
$ git commit -m 'B feature completed'
```

2. 현재 커밋 해시 값 확인해두기
```bash
$ git log
```
3. 커밋 메시지 수정
```bash
$ git commit --amend
hint: Waiting for your editor to close the file..[master c01f908] Add no.txt
...
```
4. Vim 편집기가 열리면서 직전 커밋 메시지 수정 가능
```bash
B feature completed
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# Date: Wed Jan 12 01:25:10 2022 +0900
#
# On branch master
#
# Initial commit
#
# Changes to be committed:
# new file: test.txt

```

5. 커밋 메시지를 수정하고 저장하면, 새로운 메세지로 변경되며 커밋 해시 값 또한 변경
```bash
$ git log
```

#### 커밋 재작성
1. 실수로 bar.txt를 빼고 커밋 해버린 상황을 형성
```bash
$ touch foo.txt bar.txt
$ git add foo.txt
```
```bash
$ git status
On branch master
Changes to be committed:
(use "git restore --staged <file>..." to unstage)
new file: foo.txt
Untracked files:
(use "git add <file>..." to include in what will be committed)
bar.txt
```
```bash
$ git commit -m "foo & bar"
[master 4221af6] foo & bar
1 file changed, 0 insertions(+), 0 deletions(-)
create mode 100644 foo.txt
```
```bash
$ git status
On branch master
Untracked files:
(use "git add <file>..." to include in what will be committed)
bar.txt
```
2. 누락된 파일을 staging area로 이동

```bash
$ git add bar.txt
$ git status
On branch master
Changes to be committed:
(use "git restore --staged <file>..." to unstage)
new file: bar.txt
```
3. git commit --amend를 입력
```bash
$ git commit --amend
```
4. Vim 편집기가 열리고 커밋 메시지 수정
```bash
foo & bar
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# Date: Mon Jun 7 22:32:58 2021 +0900
#
# On branch master
# Changes to be committed:
# new file: bar.txt
# new file: foo.txt

```
5. Vim 편집기를 저장 후 종료하면 직전 커밋이 덮어 씌워짐
```bash
$ git commit --amend
[master 7f6c24c] foo & bar
Date: Mon Jun 7 22:32:58 2021 +0900
2 files changed, 0 insertions(+), 0 deletions(-)
create mode 100644 bar.txt
create mode 100644 foo.txt
```
6. git log -p를 사용하여 직전 커밋의 변경 내용을 확인

#### 장점
* --amend 옵션으로 커밋을 고치는 작업이 주는 장점은 마지막 커밋 작업에서 뭔가를 빠뜨린 것을 넣거나 변경하는 것을 새 커밋으로 분리하지 않고 하나의 커밋에서 처리하는 것

#### 중요
* 이렇게 --amend 옵션으로 커밋을 고치는 작업은, 추가로 작업한 일이 작다고 하더라도 이전의 커밋을 완전히 새로 고쳐서 새 커밋으로 변경하는 것을 의미
* 이전의 커밋은 일어나지 않은 일이 되는 것이고, 당연히 히스토리에도 남지 않음


# Reset & Revert
* 둘의 공통점 : 과거로 되돌린다.
* 차이점 : 과거로 되돌리겠다는 내용이 commit에 남는가??

## git reset
* 시계를 마치 과거로 돌리는 듯한 행위로써, 특정 커밋 상태로 되돌아감
* 특정 커밋으로 되돌아 갔을 떄, 해당 커밋 이후로 쌓아놨던 커밋들은 전부 사라짐

```bash
$ git reset [옵션] <커밋 ID>
```
* 옵션
  1. --soft
    * 돌아가려는 커밋으로 되돌아가고, 이후의 commit된 파일들을 staging area로 돌려놓음(commit하기 전 상태)
    * 즉 다시 커밋할 수 있는 상태가 됨
  2. --mixed
    * 돌아가려는 커밋으로 되돌아가고, 이후의 commit된 파일들을 working directory로 돌려놓음(add하기 전 상태)
    * 즉, unstage된 상태로 남아 있음
    * 기본값
  3. --hard
    * 돌아거려는 커밋으로 되돌아가고, 이후의 commit된 파일들(tracked 파일들)은 모두 working directory에서 삭제
    * 단, Untracked파이릉ㄴ 그대로 Untracted로 남음

### 옵션별 결과
* 돌아가려는 커밋(first) 이후에 커밋된 2.txt, 3.txt가 어떻게 처리되는지 확인하기
* 시작전 커밋 확인

```bash
$ git log --oneline
20d320d (HEAD -> master) third
1eb059e second
6baf32f first
```

1. --soft
```bash
$ git reset --soft 6baf
```
* commit log의 앞의 몇글자만 적어도 적용됨

![reset soft](<../이미지/240419/reset soft.png>)

2. --mixed
```bash
$ git reset 6baf
```
![reset mixed](<../이미지/240419/reset mixed.png>)

3. --hard
```bash
$ git reset --hard 6baf
```
![reset hard](<../이미지/240419/reset hard.png>)

* 옵션 한눈에 보기
![reset 옵션한눈에 보기](<../이미지/240419/옵션 한눈에 보기.png>)

* git rest 이해하기
![git reset](<../이미지/240419/git reset.png>)

### 참고
* 이미 삭제한 커밋으로 다시 돌아가고 싶다면 git reflog를 사용
```bash
$ git reflog
1a410ef HEAD@{0}: reset: moving to 1a410ef
ab1afef HEAD@{1}: commit: modified repo.rb a bit
484a592 HEAD@{2}: commit: added repo.rb
$ git reset --hard <복구하고자 하는 커밋ID>
# git reflog 명령어는 HEAD가 이전에 가리켰던 모든 커밋을 보여줌
# 따라서 --hard 옵션을 통해 지워진 커밋도, reflog로 조회하여 돌아갈 수 있음
```

## git revert
* 특정 사건을 없었던 일로 만드는 행위로써, 이전 커밋을 취소한다는 새로운 커밋을 만듦.
* git reset은 커밋 내역을 삭제하는 반면, git revert는 새로 커밋을 쌓는 다는 차이
* git reset은 쉽게 과거로 돌아갈 수있다는 장점이 있지만, 커밋 내역이 사라진다는 단점이 있음
  * 이 때문에 다른사람과 협업할 때 커밋 내역의차이로 인해 충돌이 발생할 수 있음

```bash
$ git revert <커밋 ID>
```

### 사용 예시
* 시작전 커밋 확인
```bash
$ git log --oneline
20d320d third
1eb059e second
6baf32f first
```
* second 커밋으로 revert
```bash
$ git revert 1eb059
```

* vim 편집기가 나오면 저장 후 종료
```bash
$ git log --oneline
f0b5364 (HEAD -> master) Revert "second" # 새로 쌓인 커밋
20d320d third
1eb059e second # 히스토리는 남아있음
6baf32f first
```

* second 커밋에서 있었던 2.txt 가 사라진 것을 확인(== second 커밋을 없었던 일로 만든 것)

![git revert 예시](<../이미지/240419/git revert 예시.png>)

* git revert 이해

![git revert](<../이미지/240419/git revert.png>)

### 중요
* git reset과 비슷하다는 이유로 조심할 점
  * git reset --hard 5sd2f42라고 작성하면 5sd2f42라는 커밋으로 돌아간다는 뜻
  * git revert 5sd2f42라고 작성하면 5sd2f42라는 커밋을 되돌린다는 뜻

### 참고

```bash
# 공백을 통해 여러 커밋을 한꺼번에 되돌리기 가능
$ git revert 7f6c24c 006dc87 3551584
# 범위 지정을 통해 여러 커밋을 한꺼번에 되돌리기 가능
$ git revert 3551584..7f6c24c
# 커밋 메시지 작성을 위한 편집기를 열지 않음 (자동으로 커밋 완료)
$ git revert --no-edit 7f6c24c
# 자동으로 커밋하지 않고, Staging Area에만 올림 (이후, git commit으로 수동 커밋)
# 이 옵션은 여러 커밋을 revert 할 때 하나의 커밋으로 묶는게 가능
$ git revert --no-commit 7f6c24c
```