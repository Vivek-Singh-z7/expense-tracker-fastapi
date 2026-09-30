from conn.db import get_connection
from schemas.expense_schema import Expense

def insert_expense(expense: Expense):
  try:
    with get_connection() as conn:
      with conn.cursor() as cur:
        cur.execute("""INSERT INTO expense (title, amount, category) VALUES (%s, %s, %s) 
                    RETURNING id, title, amount, category, expense_date, created_at""", (
        expense.title,
        expense.amount,
        expense.category
        ))
        
        row = cur.fetchone()
        
      conn.commit()
      
    
    if row is None:
        return None

    return {
        "id": row[0],
        "title": row[1],
        "amount": row[2],
        "category": row[3],
        "expense_date": row[4],
        "created_at": row[5]
    }
      
        
        
  except Exception as err:
    print(f"ERROR: {err}")


  return expense


      
  
  
  