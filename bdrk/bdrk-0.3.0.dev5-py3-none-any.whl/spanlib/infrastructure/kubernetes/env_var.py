ENV_PREFIX = "BEDROCK"

# The constants declared below are injected into bdrk client library as k8s env var keys.
# Changing these will break compatibilty with current versions of the client library.
BEDROCK_ENDPOINT_ID = f"{ENV_PREFIX}_ENDPOINT_ID"
BEDROCK_SERVER_ID = f"{ENV_PREFIX}_SERVER_ID"
POD_NAME = f"{ENV_PREFIX}_POD_NAME"
POD_IP = f"{ENV_PREFIX}_POD_IP"
API_DOMAIN = f"{ENV_PREFIX}_API_DOMAIN"
API_TOKEN = f"{ENV_PREFIX}_API_TOKEN"
BEDROCK_FLUENTD_ADDR = f"{ENV_PREFIX}_FLUENTD_ADDR"
BEDROCK_FLUENTD_PREFIX = f"{ENV_PREFIX}_FLUENTD_PREFIX"
