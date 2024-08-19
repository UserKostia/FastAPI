from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
    """
    Base class for all models.
    """

    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        """
        Generates table name from class name.
        """
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)
    """
    Primary key for the model.
    """
