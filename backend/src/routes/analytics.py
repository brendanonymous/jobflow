from fastapi import APIRouter
import json
from src.visualizations import sankey

# Initialize the router with a prefix and tags for automatic documentation
analytics_router = APIRouter(
    prefix="/analytics"
)

@analytics_router.get("/sankey")
async def generate_sankey():
    """Generate a Sankey dto and return to user"""
    sankey_dto = sankey.generate_sankey_dto()

    return sankey_dto
