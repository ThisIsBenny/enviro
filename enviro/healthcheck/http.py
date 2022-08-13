from enviro.helpers import get_config
from enviro import logging
import urequests

def ping_healthcheck():
  url = get_config("healthcheck_http_url")
  logging.info(f"> send healthcheck ping to {url}")

  auth = None
  if get_config("healthcheck_http_username"):
    auth = (get_config("healthcheck_http_username"), get_config("healthcheck_http_password"))


  try:
    result = urequests.get(url, auth=auth)
    if result.status_code not in [200, 201, 202]:
      logging.error(f"  - failed to send healthcheck ping ({result.status_code} {result.reason})")
    else:
      logging.info(f"  - healthcheck ping sended")
    result.close()

  except OSError as e:
    logging.debug(E)
    logging.error(f"  - failed to send healthcheck ping")
