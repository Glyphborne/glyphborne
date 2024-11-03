import os
import platform
import sys
from typing import List

import disnake
from disnake.ext import commands
from sqlmodel import SQLModel, create_engine

from glyphborne.core.configuration import configuration

sqlite_file_name = configuration["database_file"]
sqlite_url = f"sqlite:///{sqlite_file_name}"


class Bot(commands.InteractionBot):
    def __init__(self):
        self.config = configuration
        self.engine = create_engine(sqlite_url, echo=self.config["sqlmodel_echo"])

        super().__init__(test_guilds=self.config["test_guilds"])

    def load_extensions(self, exts_list: List[str]):
        loaded_exts_count = 0
        for ext in exts_list:
            try:
                self.load_extension(ext)
                print(f"Loaded extension {ext}")
                loaded_exts_count += 1
            except Exception as exception:
                exception = f"{type(exception).__name__}: {exception}"
                print(f"Failed to load extension {ext}:\n{exception}")

        print(
            f'{loaded_exts_count} extension{"s" if loaded_exts_count != 1 else ""} loaded'
        )

    async def on_connect(self):
        print(f"Connected to {len(self.guilds)} guilds")
        print(f"Using Disnake version {disnake.__version__}")
        print(f"Using Python version {sys.version}")
        print(f"Using platform {platform.system()} {platform.release()} {os.name}")
        print(f"Successfully logged in as {self.user} (ID: {self.user.id})")

    def main(self):
        SQLModel.metadata.create_all(self.engine)
        self.load_extensions(self.config["exts"])
        self.run(self.config["token"])
