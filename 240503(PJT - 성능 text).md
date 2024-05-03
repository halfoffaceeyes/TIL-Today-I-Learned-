# 테스트 & 성능 테스트
## 테스트
* 원하는 기능이 모두 구현되었는지 확인하고, 숨겨져 있는 결함을 찾는 활동
* 여러가지 도구들을 활용하여 버그를 찾아내고 신뢰성,보안,성능 등을 검증하는 중요한 단계
* 테스트의 종류는 너무 많기 때문에 상황에 맞게 필요한 테스트를 진행해야 함
* 외우지 말고 검색을 통해 필요한 것만 찾아서 사용

## 성능 테스트
* 핵심적인 테스트 중 하나
* 특정 상황에서 시스템이 어느 정도 수준을 보이는가 혹은 어떻게 대처를 하는가를 테스트하는 과정
* 목적
    * 여러테스트를 통해 성능 저하가 발생하는 요인을 제거
    * 시장에 출시되기전에 발생할 수 있는 위험과 개선사항을 파악
    * 안정적이고 신뢰할 수 있는 제품을 빠르게 만들기 위함
* 성능테스트는 한번에 많은 사람이 요청을 보내거나 특정 사용자가 오래 사용하거나 새벽에 사용하는 경우같이 특수한 케이스를 고려해서 진행해야함
* 성능테스트도 종류가 많음

### 부하테스트(Load Testing)
* 목적 : 시스템의 신뢰도와 성능을 측정
* 임계점에 해당하는 인원이 오랜 시간동안 사용하는 경우를 테스트 == 시스템에 임계점의 부하가 계속 진행되었을때 문제가 없는지
    * 임계점 : 사용자 혹은 요청이 점점 늘어나다가, 응답시간이 급격히 느려지는 시점

### 스트레스 테스트(Stress Testing)
* 목적 : 장애 조치와 복구 절차가 효과적이고 효율적인지 확인
* 임계점 이상의 인원이 사용하는 경우를 테스트 ==  시스템에 과부하가 오면 어떻게 동작하는지

### 부하 테스트 vs 스트레스 테스트
||부하 테스트|스트레스 테스트|
|---|---|---|
|도메인|성능 테스트의 하위 집합|성능 테스트의 하위 집합|
|테스트 목적|전체 시스템의 성능 확인|중단점에서의 동작, 복구 가능성 확인|
|테스트 방법|임계점까지의 가상 유저 수를 유지하며 모니터링|중단점 이상까지 가상 유저를 점진적으로 증가|
|테스트 대상|전체 시스템|식별된 트랜잭션에만 집중하여 테스트|
|테스트 완료 시기|예상 부하가 모두 적용된 경우|시스템 동작이 중단되었을 경우|
|결과|부하 분산 문제, 최대 성능, 시간 당 서버 처리량 및 응답 시간, 최대 동시 사용자 수 등|안정성, 복구 가능성|

# API 성능 테스트
## Locust
* 오픈 소스 부하 테스트 도구
* 테스트 중 메뚜기 떼가 웹 사이트를 공격한다는 의미로 착안된 이름
* 서버에 수많은 사용자들이 동시에 들어올 때 어떤 일이 벌어지는 지를 확인하는 부하 테스트를 할 수 있는 도구
* Locust의 장점
    * 파이썬 언어로 테스트 시나리오를 간편하게 작성가능
    * 결과를 웹에서 확인할 수 있는 UI를 지원

### Locust 사용법
1. 테스트 스크립트 작성하기(공식 문서를 참조)
```py
import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1,5)

    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")
    
    @task(3)
    def view_items(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")
            time.sleep(1)
    
    def on_start(self):
        self.client.post("/login", json ={"username":"foo", "password":"bar"})
```
* HttpUser : HTTP 요청을 만드는 가상 유저
* wait_time : 작업 간 대기 시간(가상 유저가 몇초마다 요청을 보내는 지-between은 특정 범위의 랜덤 수를 제공하는 모듈)
* on_start() : 가상 유저 생성 시 실행
* @task : 유저가 실행할 작업
* @task(N) : 가중치(실행 확률)
    * N만큼 높은 확률로 작업을 수행 (위의 코드의 경우 1:3 비율로 작업을 실행함)
* self.client.get : HTTP GET 요청 전송

2. Django 서버 실행
```bash
$ py -m venv venv
$ source venv/Scripts/activate
$ py manage.py runserver
```
3. vscode 터미널 추가 & Locust 설치 및 실행
```bash
$ pip install locust
$ locust -f ./locust_test.py
```
4. Locust 정상 실행 시 터미널에 아래와 같이 접속할 수 있는 URL이 출력
    * http://localhost:8089로 접속하면 Web화면으로 확인 가능(http://0.0.0.0:8089로 접속하면 에러 발생)

![Locust 실행시 터미널](<이미지/240503/Locust 실행시 터미널.PNG>)

5. 웹 실행 화면(http://localhost:8089)

![locust web](<이미지/240503/locust 실행 web.PNG>)

6. 웹 실행 화면 - Statistics 탭
* 각 URL에 대한 요청수, 실패수, 각 기준에 대한 응답시간, 평균 응답크기, RPS등 다양한 통계내용 확인 가능
* 전체 분석은 터미널에서 터미널 종료(ctrl + c) 입력 또는 Download Data 탭의 Download Report 클릭 시 확인 가능

![웹실행 statistics](<이미지/240503/웹 실행 statistics.PNG>)

7. 웹 실행 화면 - Charts 탭

![웹 실행 charts](<이미지/240503/웹 실행 chart.PNG>)

8. 웹 실행 화면 - Failures 탭
* 실패한 요청에 대한 정보와 실패 원인이 출력

![웹 실행 Failures](<이미지/240503/Failures 탭.PNG>)

9. 웹실행 화면 - current ratio 탭
* 현재 작업이 수행된 비율을 출력

10. 웹 실행 화면 - 결과 화면(Download Data -> Download Report)

![결과화면](%EC%9D%B4%EB%AF%B8%EC%A7%80/240503/%EA%B2%B0%EA%B3%BC%ED%99%94%EB%A9%B4.PNG)

11. 콘솔 종료 화면
* 콘솔에서 Locust 종료(ctrl+c)
    * 요청시 전체 요청에 대한 분석을 콘솔에서 확인할 수 있음
![콘솔 종료](<이미지/240503/콘솔 종료 화면.PNG>)
# 정렬 알고리즘 성능 측정 실습