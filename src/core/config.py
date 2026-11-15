from pydantic import BaseModel
class AnalyticsConfig(BaseModel):
    branch: str = 'main'
    max_commits: int = 5000
    days_window: int = 90
