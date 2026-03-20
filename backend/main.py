from fastapi import FastAPI, HTTPException
import asyncpg
import os

app = FastAPI(title="Assignment 1 API")

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/assignment_db")

@app.get("/")
async def root():
    return {"message": "Welcome to the Containerized Web Application!"}

@app.get("/health")
async def health_check():
    try:
        conn = await asyncpg.connect(DATABASE_URL)
        await conn.execute('SELECT 1')
        await conn.close()
        return {"status": "ok", "db_connection": "successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")
