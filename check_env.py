# filename: check_env.py

print("check_env.py started")

from dotenv import load_dotenv
import os

load_dotenv()

print("DASHSCOPE_API_KEY exists:", bool(os.getenv("DASHSCOPE_API_KEY")))
print("DASHSCOPE_BASE_URL:", os.getenv("DASHSCOPE_BASE_URL"))
print("MODEL_NAME:", os.getenv("MODEL_NAME"))

print("check_env.py finished")