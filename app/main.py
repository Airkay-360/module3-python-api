from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.models import Idea, IdeaRequest
from app.store import IdeaStore

def create_app() -> FastAPI:
    app = FastAPI(title="Campus Idea Board")
    
    # Phase 2: Allow React frontend to call the API
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["GET", "POST"],
        allow_headers=["*"],
    )

    store = IdeaStore()  # Fresh store per app; test clients can be isolated.

    # FastAPI normally uses 422 for validation errors. We supply this handler
    # so both classroom tracks use the same 400 error contract.
    @app.exception_handler(RequestValidationError)
    async def invalid_request(request: Request, error: RequestValidationError):
        return JSONResponse(status_code=400, content={"message": "Invalid request"})

    @app.get("/api/hello")
    def hello():
        return {"message": "Hello from the Campus Idea Board! Romain!"}

    @app.get("/api/ideas")
    def get_ideas() -> list[Idea]:
        return store.find_all()

    @app.post("/api/ideas", status_code=201)
    def create_idea(request: IdeaRequest) -> Idea:
        # Phase 2: Reject empty or spaces-only titles with a 400 error
        if not request.title or not request.title.strip():
            raise HTTPException(status_code=400, detail="Title cannot be empty or spaces-only")
            
        return store.add(request)

    return app

app = create_app()