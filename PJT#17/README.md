# 과제 수행
## ssafy_학번 열 추가
![image](https://github.com/user-attachments/assets/b5bfdca5-8e68-41aa-a43a-4626409b618f)


## 정규표현식 사용
![image](https://github.com/user-attachments/assets/60e19624-c33c-46d5-b7c5-9b78e5117995)

## 위도, 경도 소수점 둘째자리 이하 절삭
![image](https://github.com/user-attachments/assets/38f6ae9e-d469-4230-890f-05659beaf18d)

## 검사기술인력수의 결측치(NULl 또는 빈 문자열)를 0으로 대체
### 채우기 이전
![image](https://github.com/user-attachments/assets/3ed2aa5c-ac05-4747-b23c-9737f1c4005b)

### 채우기 이후
![image](https://github.com/user-attachments/assets/86c222c9-b4de-4c8c-8fb6-c8642d8aa9e0)

## 서울 지역 검사소
![image](https://github.com/user-attachments/assets/d7f4338e-14e8-4a47-ada7-03f4db5ed4b5)

# Error Code: 1175
## 원인
- MySQL Workbench 등의 안전 모드(Safe Update Mode) 때문에 발생
- 이 모드는 기본 키나 조건 없이 전체 테이블을 수정하는 UPDATE/DELETE 쿼리를 막음

## 해결
### Safe Update Mode 비활성화 (권장)
MySQL Workbench 기준으로:

1. 메뉴에서 Edit → Preferences → SQL Editor 클릭
2. Safe Updates (reject UPDATEs and DELETEs with no key in WHERE clause) 체크 해제
3. 세션 종료 후 다시 연결
