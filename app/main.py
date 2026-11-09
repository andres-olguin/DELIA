"""Public API shell, deliberately fail-closed while core P0 controls remain open.

No database IO at import; no unprotected audit CRUD and no upstream requests.
Only the documentation and synthetic demonstration are suitable for publication.
"""
from fastapi import FastAPI, HTTPException
from .api import proxy

app = FastAPI(
    title="DELIA research API (DANREXO naming pending)",
    version="0.1.0-lab",
    description="Experimental only. Not a production security service.",
)
app.include_router(proxy.router)


@app.get("/")
def read_root():
    return {
        "status": "laboratory",
        "system": "DELIA / future DANREXO",
        "production_ready": False,
        "proxy_enabled": False,
    }


@app.post("/audit/")
def create_audit_log():
    # Audit read/write must await real scoped identity and tenant isolation.
    raise HTTPException(status_code=503, detail="Audit API disabled pending authentication")


@app.get("/audit/")
def get_audit_logs():
    raise HTTPException(status_code=503, detail="Audit API disabled pending authentication")
