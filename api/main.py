from fastapi import FastAPI
from dotenv import load_dotenv
from routers.journal_router import router as journal_router
import logging

load_dotenv()

# Setup basic console logging
# Use logging.basicConfig() with level=logging.INFO

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
logger.info("Starting LearningSteps API application")

app = FastAPI(title="LearningSteps API", description="A simple learning journal API for tracking daily work, struggles, and intentions")
app.include_router(journal_router)