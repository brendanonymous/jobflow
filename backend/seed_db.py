from src.database import SessionLocal
from src.models.user import User
from src.models.application import Application
from src.models.status_event import StatusEvent

with SessionLocal() as session:
    user = User(
        cognito_id="local-dev",
        email="dev@example.com",
    )

    session.add(user)
    session.flush()  # assigns user.id

    application = Application(
        user_id=user.id,
        company_name="Twilio",
        role_name="Backend Engineer",
        status_events=[
            StatusEvent(status="Applied"),
        ],
    )

    session.add(application)
    session.commit()