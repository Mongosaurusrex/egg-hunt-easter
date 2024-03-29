run-dev:
	python -m uvicorn main:app --port 8002 --reload
run:
	pm2 start "python -m uvicorn main:app --port 8002" --name "egg-hunt-2024"
