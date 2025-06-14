# calculatrice-rpn

This project exposes an API in order to manage a rpn calculator

## Setup

This project is compatible with github codespaces, or in any python>=3.12, execute the following commands
```bash
pip install -r app/requirements.txt -r tests/requirements.txt
alembic upgrade head

# To start the webserver
fastapi dev app/app.py
``` 
Then the API will be running on [http://127.0.0.1:8000](http://127.0.0.1:8000)
To access the swagger UI, go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000)

## Testing

Some tests are available, you can run them with
```bash
export PYTHONPATH=.
pytest tests
```
# Nice points
* Use sqlalchemy to support several database types
* use alembic to version database schema
* github codespace friendly
