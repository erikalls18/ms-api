
python3 /usr/src/app/db/db_setup.py
python3 /usr/src/app/db/seed_data.py

uvicorn main:app --reload --host 0.0.0.0

