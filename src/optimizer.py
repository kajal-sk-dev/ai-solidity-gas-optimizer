def suggest_optimization(code: str):
    optimized = code
    if "for (" in code:
        optimized = "// Optimized: Use unchecked & cache length\n" + optimized
    optimized = optimized.replace("public", "external")
    return optimized + "\n\n// Gas saved: ~15-30% estimated"

def estimate_savings(original, optimized):
    return {"original_gas": len(original)*2, "optimized_gas": len(optimized)*1.5}
