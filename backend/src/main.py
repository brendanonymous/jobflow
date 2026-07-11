import uvicorn
from fastapi import FastAPI
from src.routes.analytics import analytics_router
from src.routes.applications import applications_router

app = FastAPI(title="jobflow API")

for router in [analytics_router, applications_router]:
    app.include_router(router)

@app.get("/")
def root():
    return {"message": "jobflow API root"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)