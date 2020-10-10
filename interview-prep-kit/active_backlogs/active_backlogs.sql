SELECT subtable.name
FROM
(
    SELECT student.NAME AS name, student.ID
    FROM student
    INNER JOIN backlog ON student.ID = backlog.STUDENT_ID
    GROUP BY student.NAME, student.ID
    ORDER BY student.NAME ASC
) AS subtable;
