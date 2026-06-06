from fastapi import FastAPI
import uvicorn
from visualizations.router import router as visualizations_router

app = FastAPI(title="jobflow API")

app.include_router(visualizations_router)

@app.get("/")
def root():
    return {"message": "jobflow API root"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)