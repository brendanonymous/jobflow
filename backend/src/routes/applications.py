from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends
from src.database import get_session
from src.models import Application
from src.models import StatusEvent
from src.schemas.application import ApplicationCreateRequest, ApplicationCreateResponse

# Initialize the router with a prefix and tags for automatic documentation
applications_router = APIRouter(
    prefix="/applications",
    tags=["applications"],
)

# TODO: remove after cognito is integrated
# NOTE: there must be a user record with this id
LOCAL_DEV_USER_ID = 1


@applications_router.get("/")
def get_applications(session: Session = Depends(get_session)):
    """fetch and return all applications associated with user id"""
    applications = session.execute(
                        select(Application).where(Application.user_id == LOCAL_DEV_USER_ID)
                    ).scalars().all()
        
    return applications


@applications_router.post("/", status_code=status.HTTP_201_CREATED, response_model=ApplicationCreateResponse)
def create_application(request: ApplicationCreateRequest, session: Session = Depends(get_session)):
    """create a new application associated with user id"""
    application = Application(
        user_id=LOCAL_DEV_USER_ID,
        company_name=request.company_name,
        role_name=request.role_name,
    )

    if request.applied_date:
        application.applied_date = request.applied_date

    application.status_events.append(
        StatusEvent(status="Applied")
    )

    session.add(application)
    session.commit()
    session.refresh(application)

    return application