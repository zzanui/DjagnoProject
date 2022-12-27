# Django board_chat
>Django 프레임워크를 이용하여 게시판,팔로우,채팅 프로젝트 입니다.

![image](https://user-images.githubusercontent.com/103357002/209601900-f36edac8-3a1a-4f9c-8752-6e1701eb511f.png)




## 목차
___




* [프로젝트 소개](#프로젝트-소개)
* [프로젝트 기능](#프로젝트-기능)
* [사용기술](#사용기술)
* [DB설계](#DB설계)
* [실행화면](#실행화면)
* [프로젝트 보완사항](#프로젝트-보완사항)
* [후기](#후기)


## 프로젝트 소개
모르는 사람들과 친해지며 소통하여 친해질 수 있는 웹사이트가 있으면 좋겠다 생각에서 나온 프로젝트입니다.
특히 외국인이랑 대화를 할 경우 모르는 단어가 나왔을때 번역도 하며 공부도 하면 좋겠다 생각하였습니다.

## 프로젝트 기능

* 게시판 - CRUD, 페이징, 검색, 종아요
* 사용자 - auth 회원가입 및 로그인, 회원가입시 중복검사
* 댓글 - CRUD
* 프로필 - 사진,상태글
* 팔로우 - 팔로우, 언팔로우
* 채팅 - 실시간채팅, paapgo번역

## 사용기술

* 개발환경
  * Window10
  * VSCode
  * Python venv 가상환경
* 백엔드
  * 주요 프레임워크 / 라이브러리
    * python 3.9.1
    * Django 4.1.2
    * Oauth 2.0
    * Websocket
    * PapagoApi

  * DataBase
    * Sqlite
    
* 프론트엔드
  * Html/Css
  * JavaScript
  * Bootstrap 5.1.3
  
 ## DB설계
 ![image](https://user-images.githubusercontent.com/103357002/209601986-dc39448f-5078-4c9e-97ee-d3fbfa68e2a6.png)
 
 ## 실행화면
  <details>
<summary>
게시판
</summary>


**1. 게시글 전체 목록 화면**
![image](https://user-images.githubusercontent.com/103357002/209602108-ccb92800-b760-4838-a9a6-e66ad5f9c86d.png)
  모든 게시글을 조회 가능합니다. 
___

**2. 게시글 등록 화면**
![image](https://user-images.githubusercontent.com/103357002/209602127-4ed78534-52bd-46aa-a596-80bbcf6f0502.png)
  로그인 한 사용자만 게시글을 작성할 수 있습니다. 또한 작성 후 redirect합니다.
___

**3. 게시글 조회 화면**
![image](https://user-images.githubusercontent.com/103357002/209602155-6f408490-90f4-412e-9ca3-141a0f411224.png)
  본인이 작성한 글만 수정 및 삭제가 가능합니다.
___

**4. 게시글 수정 화면**
![image](https://user-images.githubusercontent.com/103357002/209602168-b0a5a385-5511-4037-b2c8-78b3249a0f2d.png)
  
  제목과 내용만 수정할 수 있게 하고 수정 후 redirect 합니다.
___

**5. 게시글 삭제 화면**
  ![image](https://user-images.githubusercontent.com/103357002/209602240-b8a2e16e-d4d4-417d-b1e8-5caa90c9bd46.png)
  삭제시 작성자 본인만 삭제가 가능하면 삭제 후 redirect합니다.
___

</details>

  <details>
<summary>
사용자
</summary>

**1. 회원가입 화면**  
![image](https://user-images.githubusercontent.com/103357002/209602268-21c3f4a8-4349-43ce-a9e4-86c416cf5f7c.png)
![image](https://user-images.githubusercontent.com/103357002/209602286-28691f18-1e70-4dd4-9aa7-9f38d12b3c0e.png)
  회원가입 시 중복확인을 진행하며 완료시 회원 정보를 저장하고 로그인 화면으로 이동합니다.

___

**2. 로그인 화면**  
![image](https://user-images.githubusercontent.com/103357002/209602308-47bcc6a8-39a5-46d3-a69c-d89b03bddc83.png)
![image](https://user-images.githubusercontent.com/103357002/209602330-2bb3266f-9d33-44a8-b555-407e45161642.png)
  로그인 시도시 로그인이 실패하였을경우 다음과 같이 알림이 나옵니다.
  네이버로그인,구글로그인과 같은 소셜로그인이 준비되어 있습니다.
</details>

  <details>
<summary>
댓글
</summary>

**1. 댓글화면**  
![image](https://user-images.githubusercontent.com/103357002/209602491-437cb6f8-75ba-4343-8325-d7f9f890ef7b.png)
___

**2. 댓글수정 화면**  
![image](https://user-images.githubusercontent.com/103357002/209602503-c5d0fcaf-a1c6-45ff-aecb-71279136828d.png)
  댓글을 작성한 본인만 수정이 가능합니다
___

**3. 댓글삭제 화면**  
![image](https://user-images.githubusercontent.com/103357002/209602529-12eb5704-d351-4c4a-b452-756bdcf4ffd9.png)
  댓글을 작성한 본인만 삭제가 가능합니다
</details>

<details>
<summary>
프로필
</summary>
**1. 프로필 조회** 

![image](https://user-images.githubusercontent.com/103357002/209603182-bb5a9900-bd30-4115-821a-8018a044ff35.png)
유저라면 누구든지 조회가 가능하며 사진,닉네임,상태메시지를 표시한다.
___

**2. 프로필 수정** 
![image](https://user-images.githubusercontent.com/103357002/209603351-e53fb703-c2df-441e-8649-a37ab11b6e92.png)
사용자 본인만 수정이 가능합니다.
___
</details>



  <details>
<summary>
팔로우
</summary>

**1. 팔로우**  

![image](https://user-images.githubusercontent.com/103357002/209602880-216577ea-4f91-4b95-b823-096e9313bd4e.png)

화면 우측에 등록중인 사용자가 전부 표시가 되며 "추가"버튼을 클릭하면 친구 테이블에 추가가 됩니다.
___

**2. 언팔로우**  
![image](https://user-images.githubusercontent.com/103357002/209602856-9bc613c3-1d57-4eba-aa12-6e488a796c47.png)

  화면 좌측에테이블에 추가되어있는 사용자가 표시되며 삭제 버튼 클릭 시 테이블에서 삭제된다
___
</details>

<details>
<summary>
채팅
</summary>
**1. 채팅**  

![image](https://user-images.githubusercontent.com/103357002/209603559-f98e7b56-8f01-4255-b81d-517f67866108.png)
팔로우창에서 대화버튼 클릭시 채팅이 가능하다
가장하단에 있는 버튼으로는 PapagoApi이용해 모르는 외국어가 있을경우 번역 가능하다
___

</details>
