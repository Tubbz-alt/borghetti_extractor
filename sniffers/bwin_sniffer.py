import urllib.request
import json
from sniffers.sniffers_config import BWIN_URL

def start_extraction_from_bwin():
    with urllib.request.urlopen(BWIN_URL) as url:
        data = json.loads(url.read().decode())
        return data