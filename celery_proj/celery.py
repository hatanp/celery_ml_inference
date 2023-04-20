from celery import Celery
import os
BROKER_URI = os.environ['BROKER_URI']
BACKEND_URI = os.environ['BACKEND_URI']

app = Celery('celery_proj',
             backend=BACKEND_URI,
             broker=BROKER_URI,
             include=['celery_proj.text_gen'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()

