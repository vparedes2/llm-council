"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Council members - list of OpenRouter model identifiers
COUNCIL_MODELS = [
    "anthropic/claude-3.5-sonnet",
    "google/gemini-pro-1.5",
    "deepseek/deepseek-chat",
    "qwen/qwen-2.5-72b-instruct",
]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "anthropic/claude-3.5-sonnet"

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
# Use /tmp on Vercel as it's the only writable directory
DATA_DIR = "/tmp/conversations" if os.getenv("VERCEL") else "data/conversations"

