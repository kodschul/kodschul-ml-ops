.PHONY: setup train track serve monitor version-data mlflow-ui

setup:
	pip install -r ../requirements.txt

train:
	python src/train.py

track:
	python src/track.py

mlflow-ui:
	mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5001

serve:
	uvicorn src.api:app --reload --port 8000

monitor:
	python src/monitor.py

version-data:
	bash scripts/version_data.sh
