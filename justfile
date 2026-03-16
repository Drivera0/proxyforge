dev-api:
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

dev-client:
    cd client && npm run dev

test:
    python -m pytest -v
