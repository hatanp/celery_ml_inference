from celery_proj.text_gen import generate
from celery.result import AsyncResult
import time
res = generate.delay("Suomen paras kaupunki on",temperature=1.0,top_p=1.0,top_k=50, do_sample=True, min_length=90, max_length=100)
res = AsyncResult(res.task_id)
start = time.time()
times = 0
while not res.ready():
    times += 1
    print(f"polled {times} times")
    time.sleep(1)
print(res.get(timeout=60))