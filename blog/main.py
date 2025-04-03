from fastapi import FastAPI
from blog.routes import routes
from blog.models import models
from blog.middleware.database import engine
import uvicorn


app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(routes.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
