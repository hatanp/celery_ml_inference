# celery_ml_inference
Examples for interacting with ML models with Celery

Requires installing suitable broker such as Redis server.

Run Celery worker with `celery -A celery_proj worker --pool=solo -l INFO` on a GPU machine. The client example can then be run on any machine