Multi-Agent Real Estate Chatbot
A sophisticated real estate assistant that combines image analysis and tenancy expertise using LangGraph and FastAPI.

Overview
This project implements a dual-agent real estate chatbot system with the following capabilities:

Image Analysis: Detects issues in property photos and provides troubleshooting advice
Tenancy Guidance: Answers rental agreement questions and explains tenant/landlord rights
Intelligent Routing: Automatically directs queries to the appropriate specialized agent
Technology Stack
FastAPI: High-performance web framework
LangGraph: Agent orchestration framework from LangChain
OpenAI GPT-4o: Multimodal AI model for text and image analysis
Pydantic: Data validation and settings management
HTML/CSS/JavaScript: Frontend interface with Tailwind CSS
Architecture
This system uses a multi-agent architecture with LangGraph to manage the state transitions between specialized agents:

Router Agent:
Determines which specialized agent should handle each query
Routes image-based queries to the Issue Detection Agent
Routes tenancy questions to the Tenancy FAQ Agent
Asks clarifying questions when the user's intent is ambiguous
Issue Detection Agent:
Analyzes uploaded property images
Identifies visible issues (water damage, mold, cracks, etc.)
Provides troubleshooting advice and recommendations
Suggests when professional help is needed
Tenancy FAQ Agent:
Handles questions about rental agreements and processes
Explains tenant and landlord rights and responsibilities
Provides jurisdiction-specific guidance when possible
Recommends legal resources when appropriate
Installation and Setup
Prerequisites
Python 3.8+
OpenAI API key
Step 1: Clone the repository
bash
git clone https://github.com/shregar1/estateAgent.git
cd estateAgent
Step 2: Set up a virtual environment
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Step 3: Install dependencies
bash
pip install fastapi uvicorn langchain langchain-openai python-multipart langgraph pydantic python-dotenv
Step 4: Create .env file with your OpenAI API key
OPENAI_API_KEY=your_api_key_here
Step 5: Run the application
bash
python app.py
The application will be available at http://localhost:8000

Usage Examples
Example 1: Image-Based Issue Detection
User Input:

Upload an image of a wall with dark spots
Text: "What's wrong with this wall?"
System Process:

Router detects image presence and routes to Issue Detection Agent
Issue Detection Agent analyzes the image using GPT-4o
Agent identifies the issue and provides recommendations
Agent Response:
"The dark spots on your wall appear to be mold growth, likely caused by excess moisture. This is common in areas with high humidity or water intrusion issues. Here's what you should do:

First, identify and fix the moisture source (leaky pipes, poor ventilation, etc.)
Improve ventilation in the room with fans or dehumidifiers
For small areas, you can clean with vinegar or a commercial mold remover
For larger infestations like this, I recommend consulting a professional mold remediation service as mold can cause health issues and may have spread behind the wall
The discoloration pattern suggests this has been developing for some time, so addressing the root cause is essential to prevent recurrence."

Example 2: Tenancy Question
User Input:
"My landlord wants to increase my rent by 25% with just two weeks' notice. I'm in California. Is this legal?"

System Process:

Router analyzes text content and routes to Tenancy FAQ Agent
Tenancy FAQ Agent processes the question with location context
Agent provides jurisdiction-specific guidance
Agent Response:
"In California, your landlord's actions would not be legal for several reasons:

Notice Period: California requires landlords to provide at least 30 days' written notice for rent increases under 10%, and 90 days' notice for increases over 10%.
Rent Control: Many California cities have rent control ordinances that limit the amount and frequency of rent increases. For example, under state law AB 1482 (California Tenant Protection Act), annual rent increases are generally capped at 5% plus the regional CPI (Consumer Price Index), not to exceed 10% total.
Proper Documentation: Rent increases must be properly documented with written notice.
I recommend:

Reviewing your lease agreement for specific terms about rent increases
Responding in writing that you're aware of California law requiring proper notice
Contacting local tenant rights organizations or legal aid for specific assistance
Consider consulting with a tenant rights attorney if the landlord persists
Would you like more information about tenant protection laws in California?"

Deployment Options
Option 1: Deploy on Heroku
Create a Procfile:
web: uvicorn main:app --host=0.0.0.0 --port=${PORT:-8000}
Create a runtime.txt:
python-3.9.7
Deploy to Heroku:
bash
heroku create
git push heroku main

