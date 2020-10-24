from environs import Env
import pathlib


class Config:
    def __init__(self):
        env = Env()
        print(pathlib.Path(__file__).parent.absolute() / ".env")
        env.read_env()
        self.token = env("TOKEN")
        # self.token ="text"


config = Config()
