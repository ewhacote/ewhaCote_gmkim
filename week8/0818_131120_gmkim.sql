/*
Programmers 131120 3월에 태어난 여성 회원 목록 출력하기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131120
*/

SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, "%Y-%m-%d") AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE DATE_OF_BIRTH LIKE '%-03-%'
AND GENDER = 'W'
AND TLNO IS NOT NULL
ORDER BY MEMBER_ID ASC;