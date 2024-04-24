# Ajax
* Asynchronous JavaScript and XML
* 비동기적인 웹 애플리케이션 개발에 사용하는 기술
## Ajax를 활용한 클라이언트 서버 간 동작
* XML 객체 생성 및 요청 -> Ajax요청 처리 -> 응답 데이터 생성 -> Json 데이터 응답 -> Promise 객체 데이터를 활용해 DOM 조작(웹 페이지의 일부분 만을 다시 로딩)
![ajax를 활용한 서버간 동작](<../이미지/240424/Ajax를 활용한 서버간 동작.PNG>)

# Ajax with Follow
## 비동기 팔로우 구현
1. M:N까지 진행한 django 프로젝트 준비
2. 가상 환경 생성 및 활성화, 패키지 설치
### Ajax 적용

1. 프로필 페이지에 axios CDN 작성
![Ajax 적용1](<../이미지/240424/Ajax 적용1.PNG>)

2. form 요소 선택을 위해 id 속성 지정 및 선택
  * action과 method 속성은 삭제(요청은 axios로 대체되기 때문)
  ![Ajax 적용2](<../이미지/240424/Ajax 적용2.PNG>)

3. form요소에 이벤트 핸들러 할당
  * submit 이벤트의 기본 동작 취소(submit이벤트는 요청이라는 후속동작이 있는데 요청을 하면 서버로부터 응답이 오기 때문에 페이지를 새로고침함, 따라서 요청이라는 후속동작을 막아줌)
  ![Ajax 적용3](<../이미지/240424/Ajax 적용3.PNG>)

4. Axios 요청 작성
* url에 작성할 user pk 가져오기
(HTML => JavaScript)
![Ajax 적용4](<../이미지/240424/Ajax 적용4.PNG>)
![Ajax 적용5](<../이미지/240424/Ajax 적용5.PNG>)
  * 'data-*' 속성
    * 사용자 지정 데이터 특성을 만들어 임의의 데이터를 HTML과 DOM 사이에서 교환할 수 있는 방법
    * 모든 사용자 지정 데이터는 JavaScript에서 dataset 속성을 통해 사용
    * HTML에서 케밥case(data-my-id)로 작성했으면 JavaScript에서는 camelCase로 변경해서 접근해야함
    * 주의사항
      1. 대소문자 여부에 상관없이 'xml'문자로 시작 불가
      2. 세미콜론 포함 불가
      3. 대문자 포함 불가
        - https://developer.mozilla.org/ko/docs/Web/HTML/Global_attributes/data-*
    ![data-*](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240424/data%EC%86%8D%EC%84%B1.PNG)

5. 요청 url 작성 마무리
![Ajax 적용6](<../이미지/240424/Ajax 적용6.PNG>)

6. 문서상 input hidden 타입으로 존재하는 csrf token 데이터를 axios로 전송
* 속성 접근 방법 ([속성명=값])
* input tag는 .value로 input에 작성한 값에 접근가능함
* https://docs.djangoproject.com/en/4.2/howto/csrf/
* axios의 문서도 확인해서 axios의 문서형태에 맞게 header에 요청을 보내야함
![Ajax 적용7](<../이미지/240424/Ajax 적용7.PNG>)
![Ajax 적용8](<../이미지/240424/Ajax 적용8.PNG>)

7. 팔로우 버튼을 토글하기 위해 현재 팔로우 상태인지 언팔로우 상태인지에 대한 상태 확인
  * Django의 view 함수에서 팔로우 여부를 파악할 수 있는 변수를 추가로 생성해 JSON타입으로 응답
  * 팔로우 상태 여부를 JavaScript에게 전달할 데이터를 작성
  * 응답은 더이상 HTML 문서가 아닌 JSON 데이터로 응답
  ![Ajax 적용9](<../이미지/240424/Ajax 적용9.PNG>)

8. 팔로우 요청 후 Django 서버로 부터 받은 데이터 확인하기
![Ajax 적용10](<../이미지/240424/Ajax 적용10.PNG>)

9. 응답 데이터 is_followed에 따라 팔로우 버튼을 토글하기
![Ajax 적용11](<../이미지/240424/Ajax 적용11.PNG>)

10. 클라이언트와 서버간 XHR 객체를 주고 받는 것을 확인하기(개발자도구의 Network 탭 이용)
![Ajax 적용12](<../이미지/240424/Ajax 적용12.PNG>)

11. 팔로잉 수와 팔로워 수 비동기 적용을 위해 해당 요소를 선택할 수 있도록 span 태그와 id 속성 작성
  ![Ajax 적용13](<../이미지/240424/Ajax 적용13.PNG>)

12. Django view 함수에서 팔로워,팔오잉 인원수 연산을 진행하여 결과를 응답 데이터로 전달
![Ajax 적용14](<../이미지/240424/Ajax 적용14.PNG>)

13. 각 span 태그를 선택하고 응답 데이터를 받아 각 태그의 인원수 값 변경에 적용
![Ajax 적용15](<../이미지/240424/Ajax 적용15.PNG>)

#### 좋아요 구현 코드
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>{{ person.username }}님의 프로필 페이지</h1>
  {% comment %} 13. 팔로잉/팔로워 수 비동기 적용 선택을 위해 span 태그 지정 {% endcomment %}
  <div>
    팔로잉 : <span id = 'followings-count'>{{ person.followings.all|length }}</span> / 
    팔로워 : <span id = 'followers-count'>{{ person.followers.all|length }}</span>
  </div>
  {% if request.user != person %}
    <div>
      {% comment %} 1. 요청은 axios로 대체되기 때문에 form 태그의 action과 method를 삭제 {% endcomment %}
      {% comment %} 6. JS에게 전달할 프로필 유저의 pk를 준비(JS에서 요청 url을 완성해야하기 때문) {% endcomment %}
      <form id = 'follow-form' data-user-id = "{{person.pk}}">
        {% csrf_token %}
        {% if request.user in person.followers.all %}
          <input type="submit" value="언팔로우">
        {% else %}
          <input type="submit" value="팔로우">
        {% endif %}
      </form>
    </div>
  {% endif %}

  <h2>{{ person.username }}님이 작성한 게시글</h2>
  {% for article in person.article_set.all %}
    <div>{{ article.title }}</div>
  {% endfor %}

  <h2>{{ person.username }}님이 작성한 댓글</h2>
  {% for comment in person.comment_set.all %}
    <div>{{ comment.content }}</div>
  {% endfor %}

  <h2>{{ person.username }}님이 좋아요한 게시글</h2>
  {% for article in person.like_articles.all %}
    <div>{{ article.title }}</div>
  {% endfor %}

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    // 2. sumbit 이벤트가 발생하는 form 태그 선택
    const formTag= document.querySelector('#follow-form')
    // 9. csrf 토큰의 value 값을 조회 및 저장
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    const userId = formTag.dataset.userId
    // 3. 선택한 form 태그에 이벤트핸들러 할당
    formTag.addEventListener('submit',function(event){
      // 4. submit 이벤트의 기본 동작을 취소
      event.preventDefault()
      // 7. HTML에서 전달하는 프로필 유저의 PK 값 조회
      console.log(event.currentTarget.dataset)
      // 5. axios 작성
      axios({
        method : 'post',
        // 8. html에서 보내준 프로필 유저의 pk를 활용해 url 완성
        url : `/accounts/${userId}/follow/`,
            // 10. 요청 header에 csrf 토큰 값 저장
        headers: {'X-CSRFToken' : csrftoken}
      })
      .then(response => {
        // console.log(response)
        // 11. 팔로우 여부를 알려주는 변수를 저장
        const isFollowed = response.data.is_followed
        // 12. isFollowed에 따라 팔로우/언팔로우 버튼 올바르게 토글
        const followBtn = document.querySelector('input[type=submit]')
        if(isFollowed== true) {
          followBtn.value = '언팔로우'
        } else {
          followBtn.value = '팔로우'
        }
        // 14. 팔로잉/팔로워 수를 출력하는 span 태그 선택
        const followingsCountTag = document.querySelector('#followings-count')
        const followersCountTag = document.querySelector('#followers-count')
        // 15. django가 계산판 팔로잉/팔로워수를 받아서 span태그의 컨텐츠를 업데이트
        followingsCountTag.textContent = response.data.followings_count
        followersCountTag.textContent = response.data.followers_count
      })
      .catch(error => {
        console.log(error)
      })
    })


  </script>
</body>
</html>

```
```py
# views.py
@login_required
def follow(request, user_pk):
    me = request.user
    you = get_user_model().objects.get(pk=user_pk)

    if me != you:
        if me in you.followers.all():
            you.followers.remove(me)
            is_followed = False
        else:
            you.followers.add(me)
            is_followed = True
        context ={
            'is_followed' : is_followed,
            'followings_count' : you.followings.count(),
            'followers_count' : you.followers.count(),
        }
        return JsonResponse(context)
    return redirect('accounts:profile', you.username, context)

```


# Ajax with likes
## 비동기 좋아요 구현
* Ajax 좋아요 적용시 유의사항
  * 전반적인 Ajax 적용은 팔로우 구현 과정과 모두 동일
  * 단, 팔로우와 달리 좋아요 버튼은 한페이지에 여러개가 존재하므로 모든 좋아요 버튼에 이벤트 리스너의 기능이 필요 ==> 하지만 모두 할당하지 않아도 됨(버블링을 사용)
* 좋아요 + ajax의 기본적인 큰 로직은 팔로우와 동일
  - 차이점 : 어떤 좋아요 버튼이 눌린건지 알아야함 ==> 버블링
  * event.currentTarget => 핸들러가 부착된 대상
  * event.target=> 실제 이벤트가 발생한 지점
  * 공통된 부모의 역할을 할 수 있는 부모 태그에만 이벤트 핸들러를 부착(버블링을 응용)
### Ajax 적용
1. 모든 좋아요 form 요소를 포함하는 최상위 요소 작성
![좋아요 Ajax1](<../이미지/240424/좋아요 ajax1.PNG>)

2. 최상위 요소 선택 및 이벤트 핸들러 할당
  * 하위 요소들의 submit 이벤트를 감지하고 submit기본 이벤트를 취소
![좋아요 Ajax2](<../이미지/240424/좋아요 ajax2.PNG>)

3. axios 작성
  * 각 좋아요 form에 article.pk 부여 후 HTML의 article.pk 값을 JavaScript에서 참조
![좋아요 Ajax3](<../이미지/240424/좋아요 ajax3.PNG>)

4. url 완성 후 요청 및 응답 확인
![좋아요 Ajax4](<../이미지/240424/좋아요 ajax4.PNG>)

5. 좋아요 버튼을 토글하기 위해서는 현재 사용자가 좋아요를 누른 상태인지 좋아요를 누르지 않은 상태인지 확인
  * Django의 view 함수에서 좋아요 여부를 파악할 수 있는 변수 추가 생성
  * JSON 타입으로 응답하기

6. 좋아요 상태 여부를 JavaScript에게 전달할 데이터 작성 및 JSON 데이터 응답
![좋아요 Ajax5](<../이미지/240424/좋아요 ajax5.PNG>)

7. 응답 데이터 is_liked를 받아 isLiked 변수에 할당
![좋아요 Ajax6](<../이미지/240424/좋아요 ajax6.PNG>)

8. isLiked에 따라 좋아요 버튼을 토글하기
  * 그런데 어떤 좋아요 버튼을 선택했는지 확인하기 위한 값이 필요
  ![좋아요 Ajax7](<../이미지/240424/좋아요 ajax7.PNG>)

9. 문자와 article의 pk 값을 혼합하여 id 속성 값을 설정
![좋아요 Ajax8](<../이미지/240424/좋아요 ajax8.PNG>)

10. 각 좋아요 버튼을 선택 후 isLiked에 따라 버튼을 토글
![좋아요 Ajax9](<../이미지/240424/좋아요 ajax9.PNG>)

### 코드
```html
<!-- articles/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  {% if request.user.is_authenticated %}
    <h2>반갑습니다, {{ user.username }} 님</h2>
    <a href="{% url "accounts:profile" user.username %}">내 프로필</a>
    <form action="{% url "accounts:logout" %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="Logout">
    </form>
    <form action="{% url "accounts:delete" %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="회원탈퇴">
    </form>
    <a href="{% url "accounts:update" %}">회원정보수정</a>
    <a href="{% url "articles:create" %}">CREATE</a>
  {% else %}
    <a href="{% url "accounts:login" %}">Login</a>
    <a href="{% url "accounts:signup" %}">Signup</a>
  {% endif %}
  <h1>Articles</h1>
  <hr>
{% comment %} 1. 전체 게시글을 포함하는 부모 태그 생성 {% endcomment %}
  <article class="article-container">

    {% for article in articles %}
    <p>
      작성자: 
      <a href="{% url "accounts:profile" article.user.username %}">{{ article.user }}</a>
    </p>
    <p>글 번호: {{ article.pk }}</p>
    <a href="{% url "articles:detail" article.pk %}">
      <p>글 제목: {{ article.title }}</p>
    </a>
    <p>글 내용: {{ article.content }}</p>
    <p><span id ='liked-count-{{article.pk}}'>{{ article.like_users.all|length }}</span> 명이 이 글을 좋아합니다.</p>
    {% comment %} <p>{{ article.like_users.count }} 명이 이 글을 좋아합니다.</p> {% endcomment %}
    {% comment %} 5. axios로 요청이 대체되기 때문에 form 태그에 action과 method를 삭제 {% endcomment %}
    {% comment %} 7. JS로 전달해줄 article의 pk 작성(어떤 게시글의 form이 동작하는 지 알아야하기 때문) {% endcomment %}
    <form data-article-id='{{ article.pk }}' >
      {% csrf_token %}
      {% if request.user in article.like_users.all %}
      <input type="submit" value="좋아요 취소" id="like-{{article.pk}}">
      {% else %}
      <input type="submit" value="좋아요" id="like-{{article.pk}}">
      {% endif %}
    </form>
    <hr>
    {% endfor %}
  </article>
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    // 2. 최상위 부모 요소인 article 태그를 선택
    const articleContainer = document.querySelector('.article-container')
    // 3. 선택한 article 태그에 이벤트 핸들러 부착
    articleContainer.addEventListener('submit', function(event) {
      event.preventDefault()
      // 8. HTML에서 전달해준 article의 pk 값을 조회 및 저장
      //console.log(event.target.dataset)
      const articleId=event.target.dataset.articleId
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
      // 4. 이벤트가 실제 동작하는 target 확인
      // console.log(event.target)
      // 6. axios 작성
      axios({
        method :'post',
        url : `/articles/${articleId}/likes/`,
        headers : {'X-CSRFToken': csrftoken},
      })
      .then((response) => {
        // console.log(response)
        // 10. 좋아요 상태 변수 값에 따라 좋아요 버튼을 올바르게 토글
        const isLiked = response.data.is_liked
        const likeBtn = document.querySelector(`#like-${articleId}`)
        if (isLiked === true) {
          likeBtn.value = '좋아요 취소'
        } else {
          likeBtn.value = '좋아요'
        }
        // 11. 몇명이 좋아요를 눌렀는지에 대한 비동기 처리
        const likedCount = response.data.liked_count
        const likedCountTag = document.querySelector(`#liked-count-${articleId}`)
        likedCountTag.textContent = likedCount

      })
      .catch((error) =>{
        console.log(error)
      })
    })
    
  </script>
  </body>
  </html>
  
```

```py
@login_required
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
        is_liked= False
    else:
        article.like_users.add(request.user)
        is_liked =True
    context ={
        'is_liked' : is_liked,
        'liked_count' : article.like_users.count(),
    }
    return JsonResponse(context)
    # return redirect('articles:index')

```

### 버블링을 활용하지 않은 경우
1. querySelectorAll()을 사용해 전체 좋아요 버튼을 선택
![queryselectorall 활용](<../이미지/240424/queryselectorall 활용.PNG>)

2. forEach()를 사용해 전체 좋아요 버튼을 순회하면서 진행
![foreach 활용](<../이미지/240424/for each 활용.PNG>)
