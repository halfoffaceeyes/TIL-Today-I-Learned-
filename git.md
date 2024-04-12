touch a.txt (a이름의 txt파일 생성)

vim a.txt (a.txt 파일 수정)-> i (insert모드로 바꿈, 내용 수정가능) -> 수정 -> esc(편집기 종료) -> :wq(vim에서 저장(write) 나오게(quit) 하는 명령어)

# Branch
* 나뭇가지처럼 여러갈래로 작업 공간을 나누어 독립적으로 작업할 수 있도록 도와주는 Git의 도구
* 협업을 위한 도구
## 장점
1. 독립 공간을 형성, 원본(Master)이 안전하다.
    * 현업에서는 마스터브랜치를 건드리지 않고 업무를 진행
    * Master(Main) 브랜치 : 사용자가 사용하고 있는 버전, 세상에 공개되어있으므로 함부로 수정하거나 버전을 되돌리거나 삭제해서는 안됨, 실제로 사용중인 서비스
2. 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적으로 협업과 개발이 가능하다.
3. 쉽게 브랜치를 생성하고 브랜치 사이를 이동할 수 있다.

## Branch를 사용해야하는 이유
* 상황예시 : 상용 중인 서비스에 발생한 에러를 해결하려면?
1. 브랜치를 통해 별도의 작업 공간을 만든다.
2. 브랜치에서 에러가 발생한 버전을 이전 버전으로 되돌리거나 삭제합니다.
3. 브랜치는 **완전하게 독립**되어있어서 작업 내용이 master 브랜치에 아무런 영향을 끼치지 못합니다.
4. 이후 에러가 해결됐다면? 그 내용을 master 브랜치에 반영할 수 있습니다.

## Branch Command
* git branch # 브랜치 목록확인
* git branch -r # 원격 저장소의 브랜치 목록 확인
* git branch <브랜치 이름> # 새로운 브랜치 생성, 이때 브랜치명은 어떤 작업을 하고 있는지 알아보기 쉽게 네이밍하는 것을 추천, 커밋이 한개 이상 있어야함
* git branch -d <브랜치 이름> # 병합된 브랜치만 삭제 가능
* git branch -D <브랜치 이름> # (주의) 강제 삭제
### git swith
현재 브랜치에서 다른 브랜치로 'HEAD'를 이동시키는 명령어
* git switch <다른 브랜치 이름> # 다른 브랜치로 이동
* git switch -c <브랜치 이름> # 브랜치를 새로 생성과 동시에 이동(create=c)
* git switch -c <브랜치 이름> <커밋 ID> # 특정 커밋 기준으로 브랜치 생성과 동시에 이동
    * 커밋 ID 확인하는 방법 git log --oneline이나, git log에서 나오는 앞의 7자리
* 주의사항
    * git switch 하기전, Working Directory 파일이 모두 버전관리가 진행 중인지 확인해야함
    * branch에서 commit을 안하고 master로 이동할 경우, 작업하고 있는 파일들이 보임
    * 한번이라도 commit을 찍는다면 독립적으로 관리하므로 반드시 독립적으로 운영하기 위해서 commit을 한번이상 해야함
    * git add 를 하지 않으면, 즉 Staging Area에 한번도 올라가지 않은 새파일은 Git의 버전관리를 받고 있지 않기 때문에 브랜치가 바뀌더라도 계속 유지 됨
    * git switch를 하기전, 워킹 디렉토리의 모든 파일이 버전관리 중 인지 확인이 필요(untracked가 있는 지 반드시 확인이 필요!)

* git log --oneline # git log를 한줄로 해당 브랜치만
* git log --oneline --all # git log를 전체를 한줄로 볼수 있음
* git log --oneline --all --graph # git log에서 어떤 커밋이 어떤 브랜치에 있는지 확인

# Branch Merging
* 분기된 브랜치를 하나로 병합
* git merge <합칠 브랜치 이름>
* local에서 하는 경우 or Remote에서 하는 경우
합치려는 main code를 브랜치로 스위치해줘야함(master를 기준으로 합치고 싶으면 현재 브랜치가 master여야함)
* 순서
    * 합치고자 하는 중심이 될 브랜치로 switch : git switch <main branch>
    * 중심 브랜치에서 합침 : git merge <합칠branch>
## Merge 종류
1. Fast-Foward Merge
* master를 분기했을 때, 마스터의 수정이 없는경우에 사용
* hotfix의 commit내용을 반영하면서 마스터가 뒤로 이동
2. 3-way-merge
* 분기 이후, master에 커밋이 있는 경우에 사용
* 기준점에서 마스터의 변경점, 브랜치의 변경점과 기준점 3가지

## Merge conflict
* 병합하는 두브랜치에서 같은 파일의 같은부분을 수정한 경우
* git은 어느 브랜치의 내용을 

충돌지점은 vscode에서 돋보기에 좌측이나 우측 꺽새를 5개 이상 입력시 찾을 수 있음
충돌한 지점에서 어떤 코드를 남길 것인지 선택 후 저장
저장 후 git add . -> git commit (-m 작성 x)-> :wq

# Undoing
git restore 보다는 git stash를 권장 (왜냐하면 stash는 수정사항을 어딘가에 저장하고 되돌리기 때문에 git stash apply를 하면 수정한 내용을 다시 적용할 수 있음)
# RESET & REVERT
* 파일 상태를 Unstaged 상태로 되돌리는 명령어(git add 취소)
git rm --cached #기존 파일을 유지하려면 cached가 반드시 필요, 기존 커밋이 없는 경우(status가 new일때)
git rm -rf cached # 대상이 폴더인 경우
git resotre --staged # 기존 커밋이 존재하는 경우(status가 modified 일때)

* 커밋을 취소하고 다시 남기고 싶을때
git commit --amend # 커밋 메시지를 수정하거나 이전 커밋을 덮어쓸때


* Reset 은 특정 커밋으로 되돌릴 때 , 해당 커밋 이후 커밋까지 전부 사라짐
* Revert는 특정 사건을 없었던 일로 만드는 행위로써, '이전 커밋을 취소한다는 새로운 커밋을 만듦'
두개의 차이는 과거로 되돌리는 커밋을 남기는 여부
--mixed add 전단계 수정된상태까지 돌아가는것
--hard 지정한 커밋으로 되돌아감




