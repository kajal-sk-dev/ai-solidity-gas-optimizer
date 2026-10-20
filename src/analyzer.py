def analyze_gas(code: str):
    issues = []
    if "for (" in code or "for(" in code:
        issues.append("Loop detected - high gas risk")
    if "storage" in code.lower():
        issues.append("Storage usage - optimize")
    gas_score = max(10, 100 - len(issues)*20 - len(code)//100)
    return {"gas_score": gas_score, "issues": issues, "lines": len(code.splitlines())}

def get_patterns():
    return ["loop", "storage", "reentrancy"]
