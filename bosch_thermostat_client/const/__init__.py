BS = 16
XMPP = "XMPP"
UUID = "uuid"

""" METHODS """
GET = "get"
PUT = "put"

GATEWAY = "gateway"
MODELS = "models"

TIMEOUT = 10

USER_AGENT = "User-Agent"
CONTENT_TYPE = "Content-Type"
APP_JSON = "application/json"

EMS = "EMS"
DEFAULT = "default"
ID = "id"
DATE = "dateTime"

HEATING_CIRCUITS = "heatingCircuits"
DHW_CIRCUITS = "dhwCircuits"
SOLAR_CIRCUITS = "solarCircuits"
HC = "hc"
NAME = "name"
DHW = "dhw"
SC = "sc"
CIRCUIT_TYPES = {
    HC: HEATING_CIRCUITS,
    DHW: DHW_CIRCUITS,
    SC: SOLAR_CIRCUITS
}
PATH = "path"
RESULT = "result"  # to not mismarch with value
TYPE = "type"
URI = "uri"
TIMESTAMP = "timestamp"
REGULAR = "regular"
AUTO = "auto"
MANUAL = "manual"

OPERATION_MODE = "operation_mode"
VALUE = "value"
MAX_VALUE = "maxValue"
MIN_VALUE = "minValue"
UNITS = "unitOfMeasure"
CURRENT_TEMP = "current_temp"
MODE_TO_SETPOINT = "mode_to_setpoint"
REFS = "refs"
HA_STATES = "hastates"
REFERENCES = "references"
STATUS = "status"
OFF = "off"
ACTIVE_PROGRAM = "activeProgram"

DEFAULT_MIN_TEMP = 0
DEFAULT_MAX_TEMP = 100
SETPOINT = "setpoint"

DAYS = {
    "Mo": "monday",
    "Tu": "tuesday",
    "We": "wednesday",
    "Th": "thursday",
    "Fr": "friday",
    "Sa": "saturday",
    "Su": "sunday",
}

DAYS_INT = [k for k in DAYS.keys()]
DAYS_INDEXES = [k for k in DAYS.values()]
DAYS_INV = [{v: k for k, v in DAYS.items()}]

MAX_REF = "max_ref"
MIN_REF = "min_ref"

HA_NAME = "haname"
BOSCH_NAME = "boschname"

MODE = "mode"
SWITCHPROGRAM = "switchprogram"
MAX = "max"
MIN = "min"
ON = "on"

FIRMWARE_VERSION = "versionFirmware"

ROOT_PATHS = ["/dhwCircuits", "/gateway", "/heatingCircuits",
              "/heatSources", "/notifications", "/system", "/solarCircuits"]
SENSORS = "sensors"
SENSOR = "sensor"
VALUES = "values"

SYSTEM_BUS = "systemBus"
