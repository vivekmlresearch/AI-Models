PYTHON ?= python

install:
	$(PYTHON) -m pip install -r requirements.txt

train:
	$(PYTHON) -m src.train --config configs/config.yaml

predict:
	$(PYTHON) -m src.predict --config configs/config.yaml

test:
	pytest -q

serve:
	uvicorn src.api:app --host 0.0.0.0 --port 8000
