PYTHON ?= python3

.PHONY: verify
verify:
	$(PYTHON) -B -m unittest discover -v
	$(PYTHON) lag_guard.py sample_lag.csv
	$(PYTHON) replay.py examples/replay.csv
