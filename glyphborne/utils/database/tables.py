from sqlmodel import Field, SQLModel


class Player(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    shillings: int = Field(default=None, primary_key=False)
