from fastapi import FastAPI, Request
from pydantic import BaseModel
from agent_controller import AgentController
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent_controller = AgentController()

class Message(BaseModel):
    role: str
    content: str

class InputBody(BaseModel):
    messages: list[Message]

"""
http://127.0.0.1:8000/run
{
    "messages": [
        {
            "role": "user",
            "content": "can i have a latte?"
        }
    ]
}

response:
{
    "role": "assistant",
    "content": "I recommend adding Sugar Free Vanilla syrup or Caramel syrup to your latte order. Additionally, you may enjoy a Croissant or a Chocolate Croissant to accompany your drink. Enjoy!",
    "memory": {
        "agent": "order_taking_agent",
        "step number": "1",
        "order": [
            {
                "item": "Latte",
                "quantity": "1",
                "price": "$4.75"
            }
        ],
        "asked_recommendation_before": true
    }
}
"""

@app.post("/run")
async def run_agent(input_body: InputBody):
    input_data = {"input": input_body.model_dump()}
    response = agent_controller.get_response(input_data)
    return response

@app.get("/")
def root():
    return {"message": "AgentController API is running"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)