# 📘 Assignment: FastAPI REST API

## 🎯 Objective

Build a simple RESTful API using **FastAPI**. Students will learn how to define endpoints, validate request data with **Pydantic**, and test their API using the built-in development server.

## 📝 Tasks

### 🛠️ 1) Create the API Skeleton

#### Description
Create a FastAPI application that runs on `localhost:8000` and includes a root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Install FastAPI (`fastapi`) and an ASGI server like Uvicorn (`uvicorn`).
- Define a FastAPI app instance in a file called `starter-code.py`.
- Add a root endpoint (`GET /`) that returns a JSON object with a welcome message.

### 🛠️ 2) Define a Data Model and CRUD Endpoints

#### Description
Create a Pydantic model for a simple resource (e.g., a "task" or "note") and implement endpoints that perform basic Create, Read, Update, and Delete (CRUD) operations using an in-memory list.

#### Requirements
Completed program should:

- Define a Pydantic model class for the resource.
- Use an in-memory list or dictionary to store items.
- Implement the following endpoints:
  - `POST /items/` to create a new item.
  - `GET /items/` to list all items.
  - `GET /items/{item_id}` to retrieve a single item by ID.
  - `PUT /items/{item_id}` to update an existing item.
  - `DELETE /items/{item_id}` to remove an item.
- Return appropriate HTTP status codes (e.g., 201 for creation, 404 if not found).

### 🛠️ 3) Run and Test Your API

#### Description
Run the FastAPI development server and verify the endpoints work using a browser or API client.

#### Requirements
Completed program should:

- Start the server using a command like:
  `uvicorn starter-code:app --reload`
- Confirm the API documentation is available at `/docs`.
- Demonstrate creating and retrieving items using the API.
