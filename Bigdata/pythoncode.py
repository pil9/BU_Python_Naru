import sqlite3

conn = sqlite3.connect("place.db")
cur = conn.cursor()

def 데이터조회(data) :
    data = ["공원", "먹거리", "바다", "기념품점", "여름", "밤", "어린이", "산"]
    for i in data:
        print(cur.execute("SELECT * FROM Tag where 태그 = i"))
    print(cur.fetchall())

    return cur.fetchall()
              
                            
    




        
