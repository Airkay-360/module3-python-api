# Campus Idea Board API (Module 3 Phase 1)
**Author:** Romain

## Overview
This is a RESTful API built with Python and FastAPI for a Campus Idea Board. It allows users to retrieve a list of ideas and submit new ones.

## How to Run
1. Open your terminal in the project folder.
2. Install the requirements: `pip install -r requirements.txt`
3. Start the server: `uvicorn app.main:app --reload --port 8080`
4. The API will run at `http://localhost:8080`

## API Endpoints
* **GET `/api/hello`**: Returns a personalized welcome message.
* **GET `/api/ideas`**: Returns a JSON list of all submitted ideas.
* **POST `/api/ideas`**: Creates a new idea. Requires a JSON body with `title` and `category`. Returns `400 Bad Request` if the title is blank.