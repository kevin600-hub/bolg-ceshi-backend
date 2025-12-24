from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel  # 修复点：这里必须是 BaseModel，不能是 Pydantic
from typing import List

app = FastAPI()

# --- 关键：解决前端 Vercel 访问报错的 CORS 设置 ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源访问，上线后可以改成你具体的 Vercel 网址
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有请求方式 (GET, POST 等)
    allow_headers=["*"],
)

# 定义数据结构
class Post(BaseModel):
    id: int
    title: str
    content: str

# 模拟一些企业数据或博客文章
fake_posts = [
    {"id": 1, "title": "Script Lion 创业日志", "content": "Linking Intelligence, Scripting Reality."},
    {"id": 2, "title": "FastAPI + Next.js 全栈架构", "content": "这是目前独立开发者最强的生产力组合。"},
    {"id": 3, "title": "Render 部署指南", "content": "注意 Start Command 必须配置正确。"}
]

@app.get("/")
def read_root():
    return {"status": "Lion Engine is Running"}

@app.get("/api/posts", response_model=List[Post])
def get_posts():
    return fake_posts
