from typing import TypedDict
from pydantic import BaseModel,Field

class Blog(TypedDict):
    title: str=Field(description="title of the blog post")
    content: str=Field(description="content of the blog post")
    
class BlogState(TypedDict):
    topic:str
    blog:Blog
    current_language:str