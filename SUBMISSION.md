# Phase 1 submission
Name: Romain
Course or section: Advanced Web Programming
Chosen track: Python FastAPI

## My campus idea
Start a coding club.

## Evidence log
*(Note: I saved all my screenshots in the `screenshots` folder on GitHub)*
1. **Personalized GET /api/hello:**
   - Method: GET | URL: `http://localhost:8080/api/hello`
   - Status: 200 OK | Response: `{"message": "Hello from the Campus Idea Board! Romain!"}`
2. **GET /api/ideas before creating:**
   - Method: GET | URL: `http://localhost:8080/api/ideas`
   - Status: 200 OK | Response: JSON array with the 2 seed ideas. 
3. **Valid POST /api/ideas:**
   - Method: POST | URL: `http://localhost:8080/api/ideas` | Body: `{"title": "Start a coding club", "category": "clubs"}`
   - Status: 201 Created | Response: `{"id": 3, "title": "Start a coding club", "category": "clubs"}` 
4. **GET /api/ideas after creating:**
   - Method: GET | URL: `http://localhost:8080/api/ideas`
   - Status: 200 OK | Response: JSON array with 3 ideas (it included my new one at the bottom).
5. **Blank title POST (400) and unchanged list:**
   - Method: POST | URL: `http://localhost:8080/api/ideas` | Body: `{"title": "", "category": "clubs"}`
   - Status: 400 Bad Request | Response: `{"message": "Invalid request"}`. 
6. **Malformed JSON POST (400):**
   - Method: POST | URL: `http://localhost:8080/api/ideas`
   - Status: 400 Bad Request | Response: `{"message": "Invalid request"}`
7. **Restart the server and GET /api/ideas (two seed ideas again):**
   - Method: GET | URL: `http://localhost:8080/api/ideas`
   - Status: 200 OK | Response: Back to just the 2 original seed ideas.

## Reflection
1. **What does a controller do?** 
   It acts like a middleman. It takes the HTTP request coming from the user (like our Postman tests), figures out what data it needs to grab or save, and then sends the right response back.
2. **How is GET different from POST?** 
   GET is just for asking the server for information (like reading the ideas list). POST is for when you actually want to send new data to the server to create something.
3. **How do JSON title and category become Python/Java data?** 
   FastAPI uses the `IdeaRequest` model to automatically read the JSON we send. It checks to make sure it matches the model, and then turns it into a normal Python object that we can use in our code.
4. **Why does our added idea disappear after restarting?** 
   Because we don't have a real database yet. We're just saving the ideas in a regular Python list in the memory, so whenever the server restarts, the code runs from scratch and the memory gets wiped.
5. **What would the React frontend need to know to use this API?** 
   It would need to know the exact URLs to fetch from (like `/api/ideas`), what HTTP method to use, and exactly how to format the JSON so the server doesn't reject it with a 400 error.

## Debugging story
- **Symptom:** I got a `500 Internal Server Error` in Postman when I first tried to test `GET /api/ideas`.
- **Hypothesis:** I checked my terminal to see what crashed, and it said `AttributeError: 'IdeaStore' object has no attribute 'read'`. I figured I was calling the wrong method name.
- **Change:** I looked inside `app/store.py` and saw the method was actually called `find_all()`, not `read()`. So I went back to `main.py` and changed `store.read()` to `store.find_all()`.
- **Observed result:** The server reloaded and the Postman GET request finally worked and gave me a 200 OK.

## Assistance disclosure
I used an AI to help figure out why my GET route was crashing and to help me write the exact assert statements for the pytest unit tests since I was getting a little stuck on the testing syntax. I made sure to run all the tests myself locally to confirm they worked.

## Automated test evidence
- **Command and summary:** `python -m pytest -v` -> 5 passed in 1.36s.
- **Two completed unit tests (names and assertions):** 
  - `test_adding_idea_stores_title_and_category`: I asserted that the returned title and category matched what I put in the request, and checked that `len(store.find_all())` equaled 3.
  - `test_two_new_ideas_receive_different_ids`: I asserted that `idea1.id != idea2.id`, that both IDs were greater than 2 (so they didn't reuse the seed ones), and that the total length became 4.
- **Completed POST API test (name and assertions):** 
  - `test_valid_post_returns_created_idea`: I checked that `response.status_code == 201`, that it returned an "id", and that the title/category matched what I sent in the test client.
- **Explain why unit tests differ from Postman requests:** Unit tests just run the Python functions directly in the code without actually needing a live web server to be running. Postman sends real network requests to the port the server is listening on.
- **Confirm no required test is skipped or disabled:** Confirmed, I deleted all the `@pytest.mark.skip` lines and all 5 tests passed green.