# Customer Support

## Generate embeddings

You have to run the `src/redo_embeddings.py` file.

## Running Web Server

For local run we can start server by running [run_local.py](src/run_local.py) file.

For production, use Dockerfile.# customer-support-chatbot

## Implementation Details

- Static embeddings stored on the dict `src/chroma_db` dir.
- Loaded once the app starts and queries made against those embeddings.
- To update the knowledge base, have to re-generate the embeddings.
- The chat is sticked to the browser, i.e. each browser session has its own chat.
  - It's implemented by http cookie. Clearing it will reset the chat history.