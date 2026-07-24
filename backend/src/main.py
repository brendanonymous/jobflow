import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.analytics import analytics_router
from src.routes.applications import applications_router


app = FastAPI(title="jobflow API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for router in [analytics_router, applications_router]:
    app.include_router(router)

@app.get("/")
def root():
    return {"message": "jobflow API root"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)