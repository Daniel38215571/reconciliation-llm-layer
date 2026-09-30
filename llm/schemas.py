from pydantic import BaseModel
from typing import Dict, Optional


class StatusBreakdown(BaseModel):
    MATCHED: int
    MISSING_IN_GATEWAY: int
    MISSING_IN_LEDGER: int
    AMOUNT_MISMATCH: int
    DUPLICATE_IN_GATEWAY: int


class ReconciliationSummary(BaseModel):
    run_id: Optional[str] = None
    reconciliation_time: str
    total_ledger_rows: int
    total_gateway_rows: int
    total_classifications: int
    status_breakdown: StatusBreakdown
    value_at_risk_kobo: int
    value_at_risk_naira: float
    value_at_risk_by_status_kobo: Dict[str, int]
    value_at_risk_by_status_naira: Dict[str, float]
