# Code Structure

## The Entrypoint - `main.py`

This is the entrypoint to the application. It does two main operations:

- Runs any new migrations on the database
- Scaffolds a http server with out REST API endpoints and starts it up on port 5000

## The Database Adapter - `db/`

This directory contains the models of the tables in the database. Every model (table) has a file of its own. This file contains an and every thing related to the models such as:

- schema definitions,
- dto objects to project sensitive information such as passwords,
- basic factory functions to use transactions instead of directly making use of the models in other parts of the app (this also serves as somewhat of a dependency injector making it easy to swap out database implementations later on),
- etc.

## The REST API - `api/`

This directory contains the main handlers for the REST API which is being served. It contains some common file as well as files for each of the routers (made for separation)

- `helpers.py` - It contains some helper functions used by all routers
- `input_models.py` - It contains the `pydantic` models for inputs expected by the different handlers which help in input validation
- other router files...

> [!TIP]
> The API spec (OpenAPI spec) can be viewed at [localhost:5000/docs](http://localhost:5000/docs) when running the app.
