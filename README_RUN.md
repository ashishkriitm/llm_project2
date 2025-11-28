1) Create project folder and paste files exactly as given.
2) Create and activate venv:
   python -m venv .venv
   .venv\Scripts\activate   (Windows) OR source .venv/bin/activate (mac/linux)
3) pip install -r requirements.txt
4) Make sure .env exists with SECRET_KEY
5) Run server:
   uvicorn app.main:app --port 8000
6) Visit http://127.0.0.1:8000/docs to test endpoints.
