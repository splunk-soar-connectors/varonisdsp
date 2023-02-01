# Define your constants here
VDSP_JSON_BASE_URL_KEY = 'base_url'
VDSP_AUTH_DATA = 'grant_type=client_credentials'
VDSP_ACCESS_TOKEN_KEY = 'access_token'
VDSP_TOKEN_TYPE_KEY = 'token_type'
VDSP_EXPIRES_IN_KEY = 'expires_in'
VDSP_REQUEST_TIMEOUT = 120

VDSP_MAX_USERS_TO_SEARCH = 5
VDSP_NON_EXISTENT_SID = -1000
VDSP_MAX_ALERTS = 50
VDSP_MAX_ALERTED_EVENTS = 5000
VDSP_THREAT_MODEL_ENUM_ID = 5821
VDSP_ALERT_STATUSES = {'open': 1, 'under investigation': 2, 'closed': 3}
VDSP_ALERT_SEVERITIES = ['high', 'medium', 'low']
VDSP_CLOSE_REASONS = {
    'none': 0,
    'resolved': 1,
    'misconfiguration': 2,
    'threat model disabled or deleted': 3,
    'account misclassification': 4,
    'legitimate activity': 5,
    'other': 6
}
VDSP_DISPLAY_NAME_KEY = 'DisplayName'
VDSP_SAM_ACCOUNT_NAME_KEY = 'SAMAccountName'
VDSP_EMAIL_KEY = 'Email'
VDSP_GET_ALERTS_ENDPOINT = '/api/alert/alert/GetAlerts'
VDSP_GET_ALERTED_EVENTS_ENDPOINT = '/api/alert/alert/GetAlertedEvents'
VDSP_UPDATE_ALET_STATUS_ENDPOINT = '/api/alert/alert/SetStatusToAlerts'
VDSP_INGEST_PERIOD_KEY = 'ingest_period'
VDSP_INGEST_ARTIFACTS_KEY = 'ingest_artifacts'
VDSP_LAST_FETCH_ID_KEY = 'last_fetch_id'
VDSP_DEFAULT_INGEST_PERIOD = '2 week'
