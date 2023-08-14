/*
Programmers 131530 가격대 별 상품 개수 구하기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131530
*/

SELECT TRUNCATE(PRICE, -4) AS PRICE_GROUP, COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY TRUNCATE(PRICE, -4)
ORDER BY TRUNCATE(PRICE, -4);