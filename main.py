from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# 允许 Next.js 跨域访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # 测试环境设为 *，生产环境填你的 Next.js 地址
    allow_methods=["*"],
    allow_headers=["*"],
)

# 模拟博客数据
posts = [
    {"id": 1, "title": "Industry Lion: 工业的未来", "content": "元技术正在改变工厂..."},
    {"id": 2, "title": "Script Lion: AI 编程提速", "content": "如何用脚本重构工作流..."}
]

@app.get("/")
def read_root():
    return {"status": "Lion Backend is Running"}

@app.get("/api/posts")
def get_posts():

    return posts
