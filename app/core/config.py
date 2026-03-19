# filename: app/core/config.py

import os
from dataclasses import dataclass

from dotenv import load_dotenv

# 读取.env
load_dotenv()

# 定义配置类
@dataclass
class Settings:
    dashscope_api_key: str
    dashscope_base_url: str
    model_name: str


def get_settings() -> Settings:
    """
    获取应用配置设置
    
    从环境变量中读取必要的配置信息，并进行验证，确保所有必需的配置项都已设置。
    
    Returns:
        Settings: 包含应用配置的 Settings 对象
    
    Raises:
        ValueError: 如果任何必需的环境变量未设置
    """
    # 从环境变量中读取配置，并去除首尾空格
    api_key = os.getenv("DASHSCOPE_API_KEY", "").strip()  # DashScope API 密钥
    base_url = os.getenv("DASHSCOPE_BASE_URL", "").strip()  # DashScope API 基础 URL
    model_name = os.getenv("MODEL_NAME", "").strip()  # 使用的模型名称

    # 验证必需的配置项
    if not api_key:
        raise ValueError("DASHSCOPE_API_KEY 未设置，请检查 .env 文件。")
    if not base_url:
        raise ValueError("DASHSCOPE_BASE_URL 未设置，请检查 .env 文件。")
    if not model_name:
        raise ValueError("MODEL_NAME 未设置，请检查 .env 文件。")

    # 返回配置对象
    return Settings(
        dashscope_api_key=api_key,
        dashscope_base_url=base_url,
        model_name=model_name,
    )