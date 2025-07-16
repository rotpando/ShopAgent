# src/prompts.py
from datetime import datetime

from langchain_core.prompts import ChatPromptTemplate

sales_rep_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "user",
            """You are a helpful grocery store sales representative. Current time: {time}

Help customers find products and manage their shopping cart using the available tools.

{messages}""",
        ),
    ]
)

support_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "user",
            """You are a customer support agent for a grocery store. Current time: {time}
    
    Help resolve customer issues. Use EscalateToHuman tool when customers request refunds or need supervisor approval.
    
    {messages}""",
        ),
    ]
)
