import disnake
from disnake.ext import commands
from sqlmodel import Session, SQLModel


class Accounts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def account(self, inter):
        pass

    @account.sub_command()
    async def create(self, inter):
        session = Session(self.bot.engine)
        self.bot.operations.create_user(session, inter.author.id, 0)
        await inter.send(f"Successfuly created user for {inter.author.id}")


def setup(bot):
    bot.add_cog(Accounts(bot))
