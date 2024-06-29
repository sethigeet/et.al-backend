# Running the App

> [!CAUTION]
> Make sure you have [setup the environment](./setting-up-env.md) before proceeding further!

> [!NOTE]
> This project uses `poetry` to manage dependencies but you may choose not to and either install dependencies manually in a manually managed virtual environment or use a different tool such as `pyenv`.
> Please look into how those tools are used. This document will give instructions on how to run the app using poetry only.

## Installing Dependencies

To install the required dependencies, run: `poetry install`

## Running the App

The root of the app is placed in [main.py](../main.py). It scaffolds a http server using `uvicorn`.
To run the app, simply run this file: `poetry run python main.py`
