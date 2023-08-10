/*
Programmers 131533 상품 별 오프라인 매출 구하기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131533
*/

SELECT p.PRODUCT_CODE, SUM(o.SALES_AMOUNT) * p.PRICE AS SALES
FROM PRODUCT p
JOIN OFFLINE_SALE o
ON p.PRODUCT_ID = o.PRODUCT_ID
GROUP BY o.PRODUCT_ID
ORDER BY SALES DESC, p.PRODUCT_CODE ASC;