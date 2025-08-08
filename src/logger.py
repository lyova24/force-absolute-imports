import logging
import sys

from src.config import config

formatter = logging.Formatter("%(message)s")
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO if not config.is_verbose else logging.DEBUG)
handler.setFormatter(formatter)

log = logging.getLogger(__name__)
log.addHandler(handler)
log.setLevel(handler.level)
