from .schemas import CreateUser


def create_user(user_in: CreateUser) -> dict:
    """
    Create a new user.

    :param
        user_in: Inputed new user

    :return:
        result status
        user dictionary
    """
    user = user_in.model_dump()
    return {"succeess": True, "user": user}
