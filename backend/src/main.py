from fastapi import FastAPI
import uvicorn
from routes.analytics import analytics_router

app = FastAPI(title="jobflow API")

app.include_router(analytics_router)

@app.get("/")
def root():
    return {"message": "jobflow API root"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)