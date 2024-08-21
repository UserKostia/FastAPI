from pydantic import ConfigDict, BaseModel


class ProductBase(BaseModel):
    """
    Basic product model.
    """

    name: str
    description: str
    price: int


class ProductCreate(ProductBase):
    """
    A model for the creation of a new product.
    """

    pass


class ProductUpdate(ProductCreate):
    pass


class ProductUpdatePartial(ProductCreate):
    name: str | None = None
    description: str | None = None
    price: int | None = None


class Product(ProductBase):
    """
    Model to product.
    """

    model_config = ConfigDict(
        from_attributes=True
    )  # Automatically determine attributes with their values
    id: int
