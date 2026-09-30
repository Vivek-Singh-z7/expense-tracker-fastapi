from conn.db import get_connection
from schemas.expense_schema import Expense


def update_expense_with_id(expense_id: int, req: Expense):
  print("ID:", expense_id)
  print("DATA:", req)
  try:
    with get_connection() as conn:
      with conn.cursor() as cur:
        cur.execute("""
          UPDATE expense
          SET title = %s,
              amount = %s,
              category = %s
          WHERE id = %s
          RETURNING id, title, amount, category, expense_date, created_at
      """, (
          req.title,
          req.amount,
          req.category,
          expense_id
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
    
    return None
    