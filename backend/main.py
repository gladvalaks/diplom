import uvicorn

import database.db

if __name__ == "__main__":
    database.db.create_db()
    uvicorn.run("app.app:app", host="127.0.0.1", port=3001, reload=True)