from fastapi import FastAPI
from fastapi.routing import APIRoute
import secrets
from src.view.main import router
from src.config import settings
from fastapi import FastAPI, Request, Response

def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"/openapi.json",
)


@app.middleware("http")
async def sticky_session_middleware(request: Request, call_next):
    # Check for existing session cookie
    session_id = request.cookies.get("session_id")

    if not session_id:
        # Generate new session ID
        session_id = secrets.token_urlsafe(16)
        # Store the session (in reality, you'd store which server handles this session)

    request.state.session_id = session_id

    response = await call_next(request)

    # Set the cookie if not already set
    if not request.cookies.get("session_id"):
        response.set_cookie(
            key="session_id",
            value=session_id,
            httponly=True,
            max_age=3600,  # 1 hour
        )

    return response

app.include_router(router)