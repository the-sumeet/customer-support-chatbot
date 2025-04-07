from fastapi import APIRouter, Form
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from starlette.responses import RedirectResponse

from src.schema.message import Message
from src.templates import templates
from src.tools.embeddings import load_vector_store
from src.tools.rag import setup_rag_chain
from src.utils.messages import get_messages, add_message

router = APIRouter()

vector_store = load_vector_store()
rag_chain = setup_rag_chain(vector_store)

@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):

    messages = get_messages(request.state.session_id)
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": id, "messages":messages}
    )


@router.post("/", response_class=HTMLResponse)
async def read_item(
    request: Request,
    query: str = Form(),
):
    add_message(
        request.state.session_id,
        Message(
            content=query,
            fromAi=False
        )
    )

    res = rag_chain.invoke(query)
    add_message(
        request.state.session_id,
        Message(
            content=res.content,
            fromAi=True
        )
    )

    return RedirectResponse("/", status_code=302)