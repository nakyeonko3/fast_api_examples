
## 일단 시작하기
---
### 목표
- 일단 시작 해보기
- 웹화면에 귀여운 애니메이션 캐릭터를 출력함
- 터치를 누르면 다른 사진으로 바뀜
- 사진 아래 download이 있음.
- download 버튼을 누르면 사진이 다운로드가 됨


### 구현 방법
1. fast api를 백엔드, 자바스크립트 html css를 프론트로 구성함
2. 백엔드 서버에서 외부 api 요청을 보내고 이미지 링크 주소를 저장함
3. route 함수를 통해 링크 주소를 프론트로 보내줌
4. 프론트에서는 get fetch를 이용해 이미지 주소가 적힌 것을 받음
5. click 이벤트가 발생시 fetch 요청을하고 화면에 이미지를 띄움
6. download 버튼을 만들어서 해당 버튼을 누르면 다운로드가 되게 구현<이부분이 조금 어렵네>