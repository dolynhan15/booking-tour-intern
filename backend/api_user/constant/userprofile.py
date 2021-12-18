from api_user.constant import Const

__all__ = ["Genders"]


class Genders(Const):
    MALE = 1
    FEMALE = 2
    OTHER = 3


GENDERS = (
    (Genders.MALE, "male"),
    (Genders.FEMALE, "female"),
    (Genders.OTHER, "other")
)
