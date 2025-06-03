from fastapi import HTTPException

def error_handler(e: Exception | None, code: int, detail: str):
  print(f"Error: {detail}")

  if e:
    print(f"Error: {e}")

  raise HTTPException(status_code=code, detail=detail)