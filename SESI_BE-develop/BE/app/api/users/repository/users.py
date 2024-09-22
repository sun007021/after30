from model.appmodel import Users
from model.schema import users_schema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


async def create_user(db: AsyncSession, user: users_schema.Users):
    db_user = Users(
        email=user.email,
        password=user.password,
        name=user.name,
        sex=user.sex,
        birth=user.birth,
        phone=user.phone,
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def get_user_by_email_or_phone(db: AsyncSession, get_user: users_schema.UserGet):
    query = select(Users).filter(
        (Users.email == get_user.email) | (Users.phone == get_user.phone)
    )
    result = await db.execute(query)
    return result.scalars().first()
