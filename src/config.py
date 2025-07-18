# src/config.py - ShopAgent Configuration
# 
# Central configuration file for ShopAgent application.
# Contains all constants, settings, and configuration parameters.
# 
# Updated: 2025-01-16 - Daily improvements
# Author: ShopAgent Team

import os
from pathlib import Path

# Project Information
PROJECT_NAME = "ShopAgent"
PROJECT_VERSION = "1.0.0"
PROJECT_DESCRIPTION = "AI-Powered Shopping Assistant"

# File Paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "dataset"
VECTOR_DB_DIR = PROJECT_ROOT / "vector_db"

# Dataset Files
PRODUCTS_CSV = DATA_DIR / "products.csv"
DEPARTMENTS_CSV = DATA_DIR / "departments.csv"
AISLES_CSV = DATA_DIR / "aisles.csv"
ORDERS_CSV = DATA_DIR / "orders.csv"
PRIOR_CSV = DATA_DIR / "order_products__prior.csv"

# Vector Database Settings
VECTOR_DB_COLLECTION = "products"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
VECTOR_DB_PERSIST_DIRECTORY = str(VECTOR_DB_DIR)

# LLM Configuration
DEFAULT_LLM_MODEL = "llama-3.3-70b-versatile"
DEFAULT_TEMPERATURE = 0.1
DEFAULT_MAX_TOKENS = 1024
GROQ_BASE_URL = "https://api.groq.com/openai/v1"

# Application Settings
DEFAULT_PORT = 8502
DEFAULT_USER_ID = 1
SESSION_TIMEOUT = 3600  # 1 hour in seconds

# UI Configuration
CHAT_HISTORY_LIMIT = 50
CART_DISPLAY_LIMIT = 20
DEBUG_MODE = os.getenv("DEBUG", "false").lower() == "true"

# Search Configuration
SEMANTIC_SEARCH_LIMIT = 5
STRUCTURED_SEARCH_LIMIT = 20
MIN_SEARCH_SIMILARITY = 0.3

# Customer Support Settings
ESCALATION_KEYWORDS = [
    "refund", "return", "complaint", "manager", 
    "supervisor", "problem", "issue", "broken"
]

# Tool Configuration
TOOL_TIMEOUT = 30  # seconds
MAX_TOOL_RETRIES = 3

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s" 