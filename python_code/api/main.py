from fastapi import FastAPI, Request
from pydantic import BaseModel
from agent_controller import AgentController

app = FastAPI()
agent_controller = AgentController()

class Message(BaseModel):
    role: str
    content: str

class InputBody(BaseModel):
    messages: list[Message]

@app.post("/run")
async def run_agent(input_body: InputBody):
    input_data = {"input": input_body.dict()}
    response = agent_controller.get_response(input_data)
    return response

@app.get("/")
def root():
    return {"message": "AgentController API is running"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)