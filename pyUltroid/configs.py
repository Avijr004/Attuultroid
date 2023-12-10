# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

import sys

from decouple import config

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Var:
    # mandatory
    API_ID = (
        int(sys.argv[1]) if len(sys.argv) > 1 else config("API_ID", default=7929680, cast=int)
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else config("API_HASH", default="39479f774ad8b88cff552290cfbd7b13")
    )
    SESSION = sys.argv[3] if len(sys.argv) > 3 else config("SESSION", default="1BVtsOKoBuxNmTI4OewSvRDy2HNUBRLuA6DFxRnhgiYvW-0k5BhUz2EOGeYVmbLLk9WYutzTWYP42BkTLF8Gqnqxgh_8OHgPjuowWOP-WhsGThqmPpNRxqg24NxjTul1pHdwmzSYalnrITdH6ZGc8eaG2IXXHjjW46HF3q1HgQYGWXtX3-ycC31Gj_PrCEq-qz9IzBVnyqSocucSHa4PqWsw2fOgD7rwlb5Yl00hAKTKUktXnzAyhRJSHnFVSjbxFi7t9lPjAuD40t40lQukcDx44ayFDgKXx72CzM463VZ1A7bRsLxSwph30ghH_J8zkHZMasuDZ6XpOEHMswVcH5FSBU5qJWQY=")
    REDIS_URI = (
        sys.argv[4]
        if len(sys.argv) > 4
        else (config("REDIS_URI", default="redis-18143.c326.us-east-1-3.ec2.cloud.redislabs.com:18143) or config("REDIS_URL", default=None"))
    )
    REDIS_PASSWORD = (
        sys.argv[5] if len(sys.argv) > 5 else config("REDIS_PASSWORD", default="RTYyiiEvKW1AeiGen5yUR7OYDbm5HRn2")
    )
    # extras
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    LOG_CHANNEL = config("LOG_CHANNEL", default=0, cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    HEROKU_API = config("HEROKU_API", default=None)
    VC_SESSION = config("VC_SESSION", default=None)
    ADDONS = config("ADDONS", default=False, cast=bool)
    VCBOT = config("VCBOT", default=False, cast=bool)
    # for railway
    REDISPASSWORD = config("REDISPASSWORD", default=None)
    REDISHOST = config("REDISHOST", default=None)
    REDISPORT = config("REDISPORT", default=None)
    REDISUSER = config("REDISUSER", default=None)
    # for sql
    DATABASE_URL = config("DATABASE_URL", default=None)
    # for MONGODB users
    MONGO_URI = config("MONGO_URI", default=None)
