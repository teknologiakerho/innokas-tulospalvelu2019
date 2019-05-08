source env/bin/activate
root=$(cd $(dirname $0); pwd)

# Tää tiedosto on vaan testailua varten,
# flaskin ajamiseen käytetään uWSGI

export ROBOSTAT_DB=$root/db.sqlite3
export ROBOSTAT_INIT=$root/app/init.py
export ROBOSTAT_CONFIG=$root/app/config.py
export FLASK_ENV=development
export FLASK_APP=webapp
