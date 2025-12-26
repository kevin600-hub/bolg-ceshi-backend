import os
from dotenv import load_dotenv
from supabase import create_client, Client
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

# 1. 加载本地 .env
load_dotenv()

# 2. 获取环境变量
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# 3. 初始化 Supabase 客户端 (这一步你之前漏掉了)
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 定义数据结构 (保持不变)
class Post(BaseModel):
    id: int
    title: str
    content: str

@app.get("/")
def read_root():
    return {"status": "New Energy Calc Lion Engine is Running"}

# --- 关键修改点：从数据库动态获取 ---
@app.get("/api/posts", response_model=List[Post])
def get_posts():
    # 使用 supabase 客户端去查询你刚才建立的 'post' 表
    # .select("*") 表示拿走所有列
    # .execute() 表示立即执行
    response = supabase.table("post").select("*").execute()
    
    # 这里的 response.data 就是一个列表，格式正好符合你的 Post 模型
    return response.data
