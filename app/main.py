from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, get_db

# Crea las tablas en PostgreSQL automáticamente al arrancar
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="TALIA Proxy & Audit Middleware", version="1.0.0")

@app.get("/")
def read_root():
    return {"status": "online", "system": "TALIA Middleware active"}

@app.post("/audit/", response_model=schemas.AuditLogResponse)
def create_audit_log(log: schemas.AuditLogCreate, db: Session = Depends(get_db)):
    db_log = models.AuditLog(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

@app.get("/audit/", response_model=list[schemas.AuditLogResponse])
def get_audit_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    logs = db.query(models.AuditLog).offset(skip).limit(limit).all()
    return logs