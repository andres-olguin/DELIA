from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, ForeignKey, JSON
from datetime import datetime
from .database import Base

class Country(Base):
    __tablename__ = "countries"

    code = Column(String(2), primary_key=True)  # ISO 3166-1 alpha-2: "CO", "CL"
    name = Column(String(100), unique=True, nullable=False)

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), unique=True, nullable=False)
    country_code = Column(String(2), ForeignKey("countries.code"), nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False, index=True)
    is_admin = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class AgentPreset(Base):
    __tablename__ = "agent_presets"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    provider = Column(String(50), nullable=False)
    model = Column(String(100), nullable=False)
    system_prompt = Column(Text)
    redaction_policy = Column(JSON, default=dict)  # categorías a enmascarar/bloquear, ej. {"EMAIL": "mask"}
    temperature = Column(Float)
    max_tokens = Column(Integer)
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False, index=True)
    preset_id = Column(Integer, ForeignKey("agent_presets.id"))  # origen de la copia; no lo vincula
    name = Column(String(100), nullable=False)
    description = Column(Text)
    provider = Column(String(50), nullable=False)
    model = Column(String(100), nullable=False)
    system_prompt = Column(Text)
    redaction_policy = Column(JSON, default=dict)
    temperature = Column(Float)
    max_tokens = Column(Integer)
    api_key_hash = Column(String(255), nullable=False, unique=True)
    is_active = Column(Boolean, default=True, nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    agent_name = Column(String(100), index=True)
    model_used = Column(String(100))
    prompt = Column(Text)
    response = Column(Text)
    tokens_used = Column(Integer, default=0)
    latency_ms = Column(Float, default=0.0)
    status = Column(String(50), default="SUCCESS")