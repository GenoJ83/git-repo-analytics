class GitAnalyticsError(Exception): pass
class InvalidRepositoryError(GitAnalyticsError): pass
class GitCommandFailedError(GitAnalyticsError): pass
