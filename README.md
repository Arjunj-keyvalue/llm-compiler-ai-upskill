# Automated Software Project Scaffolding

An agentic system that does Automated Software Project Scaffolding using a local LLM model. 

## Setup

This project uses [Poetry](https://python-poetry.org/) for dependency management.

1.  **Install Poetry:**

    If you don't have Poetry installed, follow the instructions on the [official website](https://python-poetry.org/docs/#installation).

2.  **Install dependencies:**

    Navigate to the project directory and run the following command to install the required dependencies:

    ```bash
    poetry install
    ```

3.  **Create and Activate Virtual Environment:**
    It's recommended to create a virtual environment in the project directory.

    To configure poetry to create virtual environments in the project's root, run:
    ```bash
    poetry config virtualenvs.in-project true
    ```

    After that, running `poetry install` will create a `.venv` directory in your project.

    To activate the virtual environment, run the following command:
    ```bash
    poetry shell
    ```

## Running the Application

To run the FastAPI application, use the following command:

```bash
poetry run uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.
