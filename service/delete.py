from conn.db import get_connection

def remove_expense(expense_id: int):
  try:
    with get_connection() as conn:
      with conn.cursor() as cur:
        cur.execute("SELECT * FROM expense WHERE id = %s", (expense_id,))
        row = cur.fetchone()
        
        cur.execute("INSERT INTO deleted_expense (id, title, amount, category, expense_date) VALUES(%s,%s,%s,%s,%s)", row[:5])
        
        cur.execute("delete from expense where id  = %s;", (expense_id,))
      
      
      conn.commit()        
        
        
      res = {
        "id": row[0],
        "title": row[1],
        "amount": row[2],
        "category": row[3],
        "expense_date": row[4],
        "date_time_zone": row[5] 
      }
      
      
        
    return res
  
  except Exception as err:
    print(f"ERROR: {err}")
    return None
  
def delete_permanently(expense_id: int):
  try:
    with get_connection() as conn:
      with conn.cursor() as cur:
        cur.execute("DELETE FROM deleted_expense WHERE id = %s",(expense_id,))
  
        deleted_rows = cur.rowcount
    
      conn.commit()


    return deleted_rows
    
  except Exception as err:
    print(f"ERROR: {err}")
    return None
    
  
