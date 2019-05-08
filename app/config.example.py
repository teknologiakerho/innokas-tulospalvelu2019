import os

# Flask
SECRET_KEY = "vaihda tämä"
JSON_AS_ASCII = False # Muuten flask vihaa ääkkösiä

# Robostat
ROBOSTAT_DB = os.environ["ROBOSTAT_DB"]
ROBOSTAT_INIT = os.environ["ROBOSTAT_INIT"]
ROBOSTAT_ADMIN_PASSWORD = "vaihda myös tämä"
ROBOSTAT_LOGFILE="robostat.log"
