from datetime import date

def model_lead(name, email, stage):
    return {
    "name": name,
    "email": email,
    "stage": stage,
    "created": date.today().isoformat()
  }