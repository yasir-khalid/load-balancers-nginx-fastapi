setup:
	@pip install -r requirements.txt

run: 
	@lsof -i :8000 -t | xargs kill -9
	@uvicorn main:app --reload --port 8000


