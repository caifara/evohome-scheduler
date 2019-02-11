from dotenv import load_dotenv
from evohomeclient2 import EvohomeClient
import os
import time

load_dotenv(dotenv_path="./.env")

client = EvohomeClient(os.getenv("EMAIL"), os.getenv("PW"), debug=True)
client.zone_schedules_backup('backup_zone_schedules_%s.json' % time.time())
client.zone_schedules_restore('new_zone_schedules.json')
