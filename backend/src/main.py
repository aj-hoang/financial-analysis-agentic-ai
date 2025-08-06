from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Load environment variables from .env file
# This will look for a .env file in the current directory or parent directories
load_dotenv()

app = FastAPI(
    title="Financial Analysis Agentic AI",
    description="An API for analyzing company financials using AI agents.",
    version="1.0.0"
)

class TickerRequest(BaseModel):
    ticker: str

@app.get("/")
def read_root():
    """
    Root endpoint that provides a welcome message and checks for API key presence.
    """
    # A simple check to see if an environment variable is loaded
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY", "YOUR_KEY_IS_NOT_SET")
    status = "loaded" if "YOUR_" not in api_key else "not set"
    return {
        "message": "Welcome to the Financial Analysis Agentic AI API",
        "environment_status": f"API keys are {status}."
    }

@app.post("/analyze", summary="Analyze a stock ticker")
def analyze_ticker(request: TickerRequest):
    """
    Accepts a stock ticker and triggers the AI agent crew to perform financial analysis.
    
    - **ticker**: The stock ticker symbol to analyze (e.g., "AAPL").
    """
    print(f"Analyzing ticker: {request.ticker}")
    # This is where we will trigger the CrewAI crew in the future.
    # For now, it returns a placeholder response.
    return {"message": f"Analysis for {request.ticker} has been initiated."}

# To run this application:
# 1. Make sure you are in the 'backend' directory.
# 2. Run the command: uvicorn src.main:app --reload
if __name__ == "__main__":
    import uvicorn
    # This allows running the app directly with `python src/main.py` from the `backend` dir
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
