from api_base.constant import Const

__all__ = ["Genders"]


class Genders(Const):
    Select = 0

    GENDERS = ((0, "male"), (1, "female"), (2, "other"))
