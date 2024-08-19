from asyncio import current_task

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)

from core.config import settings


class DatabaseHelper:
    """
    Helper class for database interactions.
    """

    def __init__(self, url: str, echo: bool = False):
        """
        Initializes the DatabaseHelper with the provided database URL and echo setting.
        """
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_scoped_session(self):
        """
        Returns a scoped session that is bound to the current task.
        """
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        """
        Provides a context manager for creating a database session.

        Yields:
            An async session object.
        """
        async with self.session_factory() as session:
            yield session
            await session.close()

    async def scoped_session_dependency(self) -> AsyncSession:
        """
        Provides a context manager for creating a scoped database session.

        Yields:
            An async scoped session object.
        """
        session = self.get_scoped_session()
        yield session
        await session.close()


db_helper = DatabaseHelper(
    url=settings.db_url,
    echo=settings.db_echo,
)
