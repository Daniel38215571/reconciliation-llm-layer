from llm.schemas import ReconciliationSummary


def build_context(summary: ReconciliationSummary) -> str:
    lines = []
    lines.append("RECONCILIATION SUMMARY")
    lines.append("=" * 50)
    lines.append("")
    lines.append("Run ID: " + str(summary.run_id))
    lines.append("Generated at: " + summary.reconciliation_time)
    lines.append("")
    lines.append("SCOPE")
    lines.append("  Ledger rows: " + str(summary.total_ledger_rows))
    lines.append("  Gateway rows: " + str(summary.total_gateway_rows))
    lines.append("  Total classifications: " + str(summary.total_classifications))
    lines.append("")
    lines.append("STATUS BREAKDOWN")
    lines.append("  MATCHED: " + str(summary.status_breakdown.MATCHED))
    lines.append("  MISSING_IN_GATEWAY: " + str(summary.status_breakdown.MISSING_IN_GATEWAY))
    lines.append("  MISSING_IN_LEDGER: " + str(summary.status_breakdown.MISSING_IN_LEDGER))
    lines.append("  AMOUNT_MISMATCH: " + str(summary.status_breakdown.AMOUNT_MISMATCH))
    lines.append("  DUPLICATE_IN_GATEWAY: " + str(summary.status_breakdown.DUPLICATE_IN_GATEWAY))
    lines.append("")
    lines.append("VALUE AT RISK")
    lines.append("  Total: NGN " + str(summary.value_at_risk_naira))
    lines.append("")
    lines.append("VALUE AT RISK BY STATUS (naira)")
    for status, amount in summary.value_at_risk_by_status_naira.items():
        lines.append("  " + status + ": NGN " + str(amount))
    lines.append("")
    return chr(10).join(lines)
