/*
Programmers 59410 NULL 처리하기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59410
*/

SELECT ANIMAL_TYPE,
    CASE
        WHEN NAME IS NULL THEN "No name"
        ELSE NAME
    END AS NAME,
    SEX_UPON_INTAKE
FROM ANIMAL_INS;