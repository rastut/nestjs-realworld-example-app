install:
	pip install -r requirements.txt
run-headless:
	locust --headless --print-stats -f api_benchmark.py -H http://localhost:3000 -u 1000 -r 1 -t 300s
run-ui:
	locust -f benchmark.py
