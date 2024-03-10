from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return "Hello"

@app.get("/posts")
def get_posts():
    posts = [
        {"id": 1, "title": "Post 1"},
        {"id": 2, "title": "Post 2"}
    ]
    return JSONResponse(content=posts)

# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {
#         "Title" : f"{payload['title']}",
#         "Content" : f"{payload['content']}"
#     }

class Post(BaseModel):
    title : str
    content: str

@app.post("/createposts")
def createPosts(new_post: Post):
    print(new_post.title)
    return {
        "Title" : f"{new_post.title}"
    }