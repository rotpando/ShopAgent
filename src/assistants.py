# src/assistants.py
import os
from datetime import datetime

from dotenv import load_dotenv
from langchain_core.runnables import RunnableConfig
from langchain_openai import ChatOpenAI

from .prompts import sales_rep_prompt, support_prompt
from .state import State
from .tools import (
    DEFAULT_USER_ID,
    EscalateToHuman,
    RouteToCustomerSupport,
    cart_tool,
    search_tool,
    set_thread_id,
    set_user_id,
    structured_search_tool,
    view_cart,
)

load_dotenv()
import pandas as pd

# Setup LLM - Use Groq as primary, fallback to OpenAI
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if GROQ_API_KEY:
    # Use Groq's Llama 3.3 70B - stable and reliable for tool calling workflows
    llm = ChatOpenAI(
        model="llama-3.3-70b-versatile",  # Stable model for tool calling
        api_key=GROQ_API_KEY,
        base_url="https://api.groq.com/openai/v1",
        temperature=0.1,  # Slightly higher temperature for more natural responses
        max_tokens=1024,  # Standard token limit
    )
elif OPENAI_API_KEY:
    # Fallback to OpenAI if available
    llm = ChatOpenAI(api_key=OPENAI_API_KEY)
else:
    # Default configuration - will fail gracefully
    llm = ChatOpenAI(api_key="dummy-key")

# Tool registration - reduced set for testing
sales_tools = [
    search_tool,
    RouteToCustomerSupport,
]
support_tools = [EscalateToHuman]

# Runnable pipelines
sales_runnable = sales_rep_prompt.partial(time=datetime.now) | llm.bind_tools(
    sales_tools,
    tool_choice="auto"  # Force auto tool selection
)
support_runnable = support_prompt.partial(time=datetime.now) | llm.bind_tools(
    support_tools,
    tool_choice="auto"  # Force auto tool selection
)

def sales_assistant(state: State, config: RunnableConfig, runnable=sales_runnable) -> dict:
    """
    LangGraph node function for running the sales assistant LLM agent.

    This function binds a chat prompt (`sales_rep_prompt`) with tools and invokes
    the LangChain Runnable pipeline. It sets the thread and user IDs and runs the
    agent with the given state and config.

    ---
    Arguments:
    - state (State): LangGraph state with current dialog history.
    - config (RunnableConfig): Config object that contains the `thread_id`.
    - runnable: (optional) The runnable to use; defaults to global `sales_runnable`.

    ---
    Behavior:
    - Extract thread ID from config and set it using `set_thread_id(...)`.
    - Set default user ID via `set_user_id(...)`.
    - Use the given `runnable` to run the assistant logic.

    ---
    Returns:
    - A dictionary with a `"messages"` key containing the new AI message(s).
    Example: `{"messages": [AIMessage(...)]}`
    """
    # Extract thread ID from config and set it for session management
    thread_id = config["configurable"]["thread_id"]
    set_thread_id(thread_id)
    
    # Set default user ID for cart and history operations
    set_user_id(DEFAULT_USER_ID)
    
    # Invoke the sales runnable with the current state and config
    response = runnable.invoke(state, config=config)
    
    # Return the response in the expected format
    # Handle both single message and list of messages
    if isinstance(response, list):
        return {"messages": response}
    else:
        return {"messages": [response]}


def support_assistant(state: State, config: RunnableConfig) -> dict:
    set_thread_id(config["configurable"]["thread_id"])
    response = support_runnable.invoke(state, config=config)
    
    # Handle both single message and list of messages
    if isinstance(response, list):
        return {"messages": response}
    else:
        return {"messages": [response]}
