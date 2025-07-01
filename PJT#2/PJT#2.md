## Procedure

```sql
DELIMITER //

CREATE PROCEDURE user_insert (
    IN user_id VARCHAR(20),
    IN user_name VARCHAR(20),
    IN user_campus VARCHAR(20),
    IN user_class VARCHAR(20),
    IN user_gi VARCHAR(20)
)
BEGIN
    INSERT INTO ssafy_user(id, name, campus, class, gi)
    VALUES(user_id, user_name, user_campus, user_class, user_gi);
END //

DELIMITER ;
```
1. "" 안에 procedure의 이름을 쓰니 오류가 나서 "" 삭제
2. `BEGIN - END` 구문 사용에서 오류가 나 DELIMITER 사용

## user insert 실행
![image](https://github.com/user-attachments/assets/21955534-8a46-418d-940a-5c172211d307)

## 전체 실행 화면
![image](https://github.com/user-attachments/assets/e37354ae-e46d-4bd4-b789-b786c5213fa8)

## 수행 과정
1. MySQL 의 비밀번호를 잊어서 삭제 후 다시 설치하는 과정에서 문제가 많았음.
2. WorkBench에서 모든 사항 삭제 후 재설치, 비밀번호 재설정으로 해결
