# Git Workflow

- Branch와 Pull request를 이용한 협업

## Feature Branch Workflow
* 팀 협업 시에는 리모트에서 Merge 진행
* 개발 branch에서 push (git push origin <본인의 브랜치명>)

### Shared repository model(저장소의 소유권이 있는 경우)

1. 각 사용자는 원격 저장소의 소유권을 가진 상태, 따라서 clone을 통해 저장소를 로컬에 복제
2. 기능 추가를 위해 branch 생성 및 기능 구현
3. 기능 구현 후 원격 저장소에 브랜치 반영
4. 각 branch를 Pull request를 통해 merge, 병합 완료 된 브랜치를 삭제
5. 각 사용자는 master 브랜치로 switch
6. master 브랜치에서 병합된 내용을 pull하여 update
7. 원격 저장소에서 병합 완료된 로컬 브랜치를 삭제
8. 새로운 기능 추가를 위해 branch 생성 및 과정을 반복

### Forking Workflow

- Fork & Pull model(저장소의 소유권이 없는 경우)
1. 소유권이 없는 원격 저장소를 fork를 통해 복제(upstream -> origin)
2. 사용자가 복제한 저장소(origin)를 clone을 통해 로컬에 복제
3. 추후 로컬 저장소를 원본 원격 저장소(upstream)와 동기화 하기 위해 URL을 연결
```bash
$ git remote add upstream [원본 URL]
```
4. 기능 추가를 위해 branch 생성 및 기능 구현
5. 기능 구현 후 원격 저장소(origin)에 브랜치 반영
```bash
$ git push origin [브랜치명]
```
6. 원본(upstream)에 Pull request 요청

7. 병합 완료되면 origin에 있는 브랜치 삭제후 사용자는 로컬에서 master 브랜치로 switch
8. upstream에 병합된 master의 내용을 pull하고 로컬에 있는 병합이 완료된 브랜치를 삭제
```bash
$ git pull upstream master
```
9. 새로운 기능 추가를 위해 branch 생성 및 과정 반복
![git workflow](<../이미지/240419/git workflow.png>)