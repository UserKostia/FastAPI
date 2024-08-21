from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Product
from .schemas import ProductCreate, ProductUpdate, ProductUpdatePartial


async def get_products(session: AsyncSession) -> list[Product]:
    """
    Get all products from the database.

    :param
        session: SQLAlchemy session object.

    :return
         A list of Product objects.
    """
    stmt = select(Product).order_by(Product.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)


async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    """
    Get a product by its ID.

     :param
        session: SQLAlchemy session object.
        product_id: The ID of the product to retrieve.

    :return
        A Product object if found, otherwise None.
    """
    return await session.get(Product, product_id)


async def create_product(session: AsyncSession, product_in: ProductCreate) -> Product:
    """
    Create a new product in the database.

    :param
        session: SQLAlchemy session object.
        product_in: A ProductCreate object containing the new product data.

    :return
        The newly created Product object.
    """
    product = Product(**product_in.model_dump())
    session.add(product)
    await session.commit()
    # await session.refresh(product) # use this if you need to update the product object with the auto-generated ID
    print(f"{product = }")
    return product


async def update_product(
    session: AsyncSession,
    product: Product,
    product_update: ProductUpdate | ProductUpdatePartial,
    partial: bool = False,
) -> Product:
    for name, value in product_update.model_dump(exclude_unset=partial).items():
        setattr(product, name, value)
    await session.commit()
    return product


async def update_product_partial(
    session: AsyncSession,
    product: Product,
    product_update: ProductUpdatePartial,
) -> Product:
    for name, value in product_update.model_dump(exclude_unset=True).items():
        setattr(product, name, value)
    await session.commit()
    return product


async def delete_product(session: AsyncSession, product: Product) -> None:
    await session.delete(product)
    await session.commit()
