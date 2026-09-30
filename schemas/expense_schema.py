from pydantic import BaseModel, field_validator

class Expense(BaseModel):
  title: str
  amount: int
  category: str
  
  
  @field_validator("title", "category")
  @classmethod
  def validate_text(cls, value):
    value = value.strip().lower()
    
    if not value:
      raise ValueError("field cannot be empty")

    return value
    

  @field_validator("amount")
  @classmethod
  def validate_amount(cls, value):
    if value <= 0:
      raise ValueError("amount must be greater than 0")

    return value
