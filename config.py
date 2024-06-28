"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021  Asad Ali <https://github.com/jankarikiduniya>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "27983733")
        self.API_HASH: str = os.environ.get("API_HASH", "56ca4efd9003ada32e79409505a34ec1")
        self.SESSION: str = os.environ.get("SESSION", "1BVtsOI0Bu68456EREmx6PjbFEjeho5mT3SaeRxrh-Eyqd_8PCR8PFLyjQ2isNNrc-Lt563NVexQdh_ho6ltY1VYgNCBemY-FySTuXASuLYQ30nXjHGQOVO0QtFDR2K9BZxfWM08XB3Q-escf11Z_nRF67ApdagD2Ndeu8nq3SE1HkCZJ6k8gfv7N9wce7WwZhyA2gueiUofy7r9KM25-nZjPvOv4Gglc2LFg9k2SMfmuwvSiqSzBYL8EhpGRi1bq3GzqVhL_W40KVFvFx5BP3-xgTP63pyphYHr-tk_U4SaKC_t5db7n6Bdh7uQOiJiRsQ35imSL-VhC4AKXfaAmj_JXjpXep4o=")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", " ").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("Error: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.CUSTOM_QUALITY: str = os.environ.get("CUSTOM_QUALITY", "high").lower()


config = Config()
