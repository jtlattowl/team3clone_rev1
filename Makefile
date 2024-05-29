# Define Python version and virtual environment name
PYTHON_VERSION = python3
VENV_NAME = venv

install: 
	@echo "Installing dependencies..."
	$(PYTHON_VERSION) -m pip install -r requirements.txt

create_venv:
	@echo "Creating virtual environment..."
	$(PYTHON_VERSION) -m venv $(VENV_NAME)

activate:
	@echo "Activating virtual environment..."
	@echo "Run 'source $(VENV_NAME)/bin/activate' (Unix) or '$(VENV_NAME)\Scripts\activate' (Windows)"

initialize_git:
	@echo "Initialize git repository..."
	git init 

setup: create_venv install initialize_git
	@echo "Setup complete. Run 'make activate' to see how to activate the virtual environment."

clean:
	@echo "Cleaning up..."
	rm -rf $(VENV_NAME)

