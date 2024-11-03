from sqlmodel import Field, SQLModel


class Player(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    display_name: str

    shillings: int

    hair_color: str
    skin_color: str
