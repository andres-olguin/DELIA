import pytest
from sqlalchemy.exc import IntegrityError

from app import models
from app.database import Base, SessionLocal, engine

@pytest.fixture
def db():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

def company(db, name="Acme", country="CO"):
    db.add_all([models.Country(code=country, name=country)])
    c = models.Company(name=name, country_code=country)
    db.add(c)
    db.commit()
    return c

def test_user_defaults_and_unique_email(db):
    c = company(db)
    db.add(models.User(email="a@x.co", password_hash="h", company_id=c.id))
    db.commit()
    u = db.query(models.User).one()
    assert u.is_admin is False and u.created_at is not None
    db.add(models.User(email="a@x.co", password_hash="h", company_id=c.id))
    with pytest.raises(IntegrityError):
        db.commit()

def test_company_name_unique(db):
    company(db)
    db.add(models.Company(name="Acme", country_code="CO"))
    with pytest.raises(IntegrityError):
        db.commit()

def test_agent_is_independent_of_preset(db):
    c = company(db)
    p = models.AgentPreset(company_id=c.id, name="p", provider="openai", model="m",
                           redaction_policy={"EMAIL": "mask"})
    db.add(p)
    db.commit()
    a = models.Agent(company_id=c.id, preset_id=p.id, name="a", provider=p.provider,
                     model=p.model, redaction_policy=dict(p.redaction_policy), api_key_hash="k1")
    db.add(a)
    db.commit()
    p.model = "otro"
    db.commit()
    db.refresh(a)
    assert a.model == "m" and a.is_active is True

def test_agent_api_key_hash_unique(db):
    c = company(db)
    for _ in range(2):
        db.add(models.Agent(company_id=c.id, name="a", provider="o", model="m", api_key_hash="k"))
    with pytest.raises(IntegrityError):
        db.commit()
