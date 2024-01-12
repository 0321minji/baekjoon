SELECT PT_NAME, PT_NO, GEND_CD, AGE, COALESCE(TLNO,'NONE') AS TLNO
FROM PATIENT
WHERE AGE<=12 AND GEND_CD='W'
ORDER BY AGE DESC, PT_NAME

-- oracle에서는 NVL(기본 값, NULL일 때 넣어줄 값)
-- mysql에서는 INFULL
-- COALESCE(A,'A의값이 없는 경우의 값')   >> * 모든 데이터베이스에서 사용


