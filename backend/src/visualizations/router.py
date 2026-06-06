from fastapi import APIRouter, HTTPException
import json
from visualizations import utils

# Initialize the router with a prefix and tags for automatic documentation
router = APIRouter(
    prefix="/visualizations"
)

@router.get("/sankey")
async def generate_sankey():
    """Generate a Sankey data model and return to user"""
    sankey_data_model = utils.generate_sankey_data_model()

    return sankey_data_model
