from datetime import datetime

def get_current_time():
    """Returns the current UTC time in ISO 8601 format without timezone information."""
    current_time_utc = datetime.utcnow()
    iso_format = current_time_utc.replace(microsecond=0).isoformat()
    return iso_format