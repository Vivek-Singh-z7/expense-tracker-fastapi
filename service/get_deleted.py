from conn.db import get_connection



def show_deleted_expense() -> list[tuple]:
  try:
    with get_connection() as conn:
      with conn.cursor() as cur:
        result = []
        
        
        cur.execute("""SELECT * FROM deleted_expense ORDER BY ID ASC;""")
        rows = cur.fetchall()
        
        for row in rows:
          result.append({
            "id": row[0],
            "title": row[1],
            "amount": row[2],
            "category": row[3],
            "expense_date": row[4],
            "date_time_zone": row[5]
          })
         
        return result
  except Exception as err:
    print(F"ERROR: {err}")
    
    return []