#@title Code that reads the settings
# A setting comes from an environment variable of the same name, else from a line NAME=value in the file .env,
# else from the value in the Settings cell. A value from outside is turned into the type of that value.
import json, os

_DOTENV = {}
if os.path.isfile(".env"):
    with open(".env", encoding="utf-8") as _f:
        for _line in _f:
            _name, _sep, _value = _line.strip().partition("=")
            if _sep and not _name.startswith("#"):
                _DOTENV[_name.strip()] = _value.strip().strip("\"'")


def setting(name, default):
    raw = os.environ.get(name, _DOTENV.get(name))
    if raw is None:
        return default
    if isinstance(default, bool):
        if raw.strip().lower() in ("1", "true", "yes", "on"):
            return True
        if raw.strip().lower() in ("0", "false", "no", "off", ""):
            return False
        raise ValueError(f"{name} must be True or False, not {raw!r}")
    if isinstance(default, (int, float)):
        try:
            return type(default)(raw)
        except ValueError:
            raise ValueError(f"{name} must be a number, not {raw!r}") from None
    if isinstance(default, (list, dict)):
        return json.loads(raw)
    return raw
