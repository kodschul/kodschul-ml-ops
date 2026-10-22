.PHONY: setup train serve monitor version-data

setup:
	pip install -r ../requirements.txt

train:
	python src/train.py

serve:
	uvicorn src.api:app --reload --port 8000

monitor:
	python src/monitor.py

version-data:
	bash scripts/version_data.sh
