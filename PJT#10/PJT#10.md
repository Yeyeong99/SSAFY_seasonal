# CREATE TABLE
```sql
CREATE TABLE tbl_event (
	event_seq INT NOT NULL AUTO_INCREMENT,
    event_data INT NULL,
    reg_date DATETIME NULL,
    PRIMARY KEY (`event_seq`))
COMMENT = 'EVENT SCHEDULER TEST';
```

# SET SCHEDULER
```SQL
-- 1분마다 데이터 삽입
CREATE EVENT
	IF NOT EXISTS evt_insert_event
ON SCHEDULE
	EVERY 1 MINUTE
COMMENT 'INSERT DATA EVERY 1 MINUTE'
DO
	INSERT INTO tbl_event(event_data, reg_date)
    VALUES(1, NOW());
    
-- 5분마다 삭제
CREATE EVENT
	IF NOT EXISTS evt_delete_event
ON SCHEDULE
	AT CURRENT_TIMESTAMP + INTERVAL 5 MINUTE
COMMENT 'DELET DATA AFTER 5 MINUTES'
DO
	DELETE FROM tbl_event;
    
-- 특정 기간 반복되는 스케줄러: 3 분간 20초 마다 업데이트
CREATE EVENT
	IF NOT EXISTS evt_update_event
ON SCHEDULE
	EVERY 20 SECOND
    STARTS CURRENT_TIMESTAMP
	ENDS CURRENT_TIMESTAMP + INTERVAL 3 MINUTE
COMMENT 'UPDATE DATA EVERY 20 SECOND FOR 3 MINUTES'
DO
	UPDATE tbl_event SET event_data = event_data + 1;
```

# 결과 확인
![image](https://github.com/user-attachments/assets/d7d5aa7a-58b7-4a70-b6b2-7cf2be4dab43)
