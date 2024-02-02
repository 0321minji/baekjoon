-- 코드를 입력하세요
# SELECT *,COUNT(*)
# FROM MEMBER_PROFILE M JOIN REST_REVIEW R 
# ON M.MEMBER_ID = R.MEMBER_ID
# GROUP BY R.MEMBER_ID
# ORDER BY COUNT(*) DESC

SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE,'%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE M JOIN (
                            SELECT MEMBER_ID, REVIEW_TEXT, REVIEW_DATE
                            FROM REST_REVIEW AS RR
                            WHERE RR.MEMBER_ID = (SELECT MEMBER_ID
                                              FROM REST_REVIEW
                                              GROUP BY MEMBER_ID
                                              ORDER BY COUNT(*) DESC
                                              LIMIT 1)) AS R
ON M.MEMBER_ID = R.MEMBER_ID
ORDER BY REVIEW_DATE , REVIEW_TEXT