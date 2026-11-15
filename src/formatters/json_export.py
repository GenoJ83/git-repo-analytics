import json
def export_analytics_json(metrics: dict) -> str:
    return json.dumps(metrics, indent=2)
