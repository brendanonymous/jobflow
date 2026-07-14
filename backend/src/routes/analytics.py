from fastapi import APIRouter
import json
from src.visualizations import sankey

# TODO: remove after cognito is integrated
# NOTE: there must be a user record with this id
LOCAL_DEV_USER_ID = 1

# Initialize the router with a prefix and tags for automatic documentation
analytics_router = APIRouter(
    prefix="/analytics",
    tags=["analytics"],
)

# TODO: adapt to new backend architecture and return a Sankey dto instead of a JSON string
# TODO: seed the database with my applications and status events for testing purposes
@analytics_router.get("/sankey")
def generate_sankey():
    """Generate a Sankey dto and return to user"""
    # get all applications and status events from the db
    applications = session.execute(
        select(Application)
        .where(Application.user_id == LOCAL_DEV_USER_ID)
    ).scalars().all()

    for application in applications:
        print(f"company: {application.company_name}")
        for status_event in application.status_events:
            print(f"status: {status_event.status}, date: {status_event.date}")

    # create an ordered list of status_events

    # adapt to dto format for sankey diagram

    sankey_dto = sankey.generate_sankey_dto()

    return sankey_dto
