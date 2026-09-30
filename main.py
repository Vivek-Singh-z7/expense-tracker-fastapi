from conn import db
from fastapi import FastAPI, HTTPException
from service import add_expense, get_data, update, delete
from schemas.expense_schema import Expense 
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


db.create_db()
db.create_tables()



@app.get("/expense_tracker_app")
def show_all_expense():
  
  result =  get_data.get_data()
  
  if not result:
    raise HTTPException(
      status_code=404,
      detail="expense not found"
    )
    
  return result
  
  
@app.get("/expense_tracker_app/{expense_id}")
def show_expense(expense_id: int):
  
  result = get_data.get_data(expense_id)
  if not result:
    raise HTTPException(
      status_code=404,
      detail=f"expense not found at expense_id = {expense_id}"
    )
  return result[0]
    

@app.post("/expense_tracker_app")
def create_expense(req : add_expense.Expense):
  expense = add_expense.insert_expense(req)
  
  return {
    "message": "Expense added successfully",
    "expense": expense
}
  
@app.put("/expense_tracker_app/{expense_id}")
def update_expense(expense_id: int,  req: Expense):
  result = update.update_expense_with_id(expense_id, req)

  if result is None:
    raise HTTPException(
      status_code=404,
      detail="Expense Not Found"
    )

  
  return {
    "message": "Expense updated successfully",
    "expense": result
  }
  
  
  
@app.delete("/expense_tracker_app/{expense_id}")
def delete_expense(expense_id: int):
  result = delete.remove_expense(expense_id)
  
  if result is None:
    raise HTTPException(
      status_code=404,
      detail="Expense Not Found"
    )
    
  return result
  
  
# {
#   "title": "hair cut",
#   "amount": 50,
#   "category": "personal"
# }