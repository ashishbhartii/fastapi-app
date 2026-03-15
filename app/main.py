from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "CI/CD Pipeline Working, ------Extra Line added to check------"}
