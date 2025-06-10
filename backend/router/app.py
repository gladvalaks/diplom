import fastapi
import routes

app = fastapi.FastAPI()

for router in routes:
    app.include_router(router)

