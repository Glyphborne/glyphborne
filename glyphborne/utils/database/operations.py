from sqlmodel import Session

from glyphborne.utils.database.tables import Player


class operations:
    def create_user(session: Session, id: int, shillings: int):
        new_user = Player(id=id, shillings=shillings)
        session.add(new_user)
        session.commit()
