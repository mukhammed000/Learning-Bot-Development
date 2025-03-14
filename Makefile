# Use the default Python interpreter
PYTHON := python3

# Define the main script
MAIN_SCRIPT := first.py

.PHONY: run

# Run the Python script
run:
	$(PYTHON) $(MAIN_SCRIPT)

# Clean up temporary files (if needed)
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
