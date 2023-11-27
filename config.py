from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 1331889
    API_HASH = "b6f525900fd20d4282116c6fe13094ac"
    # the name to display in your alive message
    ALIVE_NAME = "Edikur.exe STORE"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://rzohiejw:Ek-PSjVmyrfiyi4iceb-dPfEwY2RB1Jp@batyr.db.elephantsql.com/rzohiejw"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOJwBu1jJWNH--cZw_PIvNC3m3UjlYUUKauYl5TdpeQeDZywYK6uHU6zDnU9FLQDxa5vr4wn8r3J-O15RMyEPnc_6JdMDqJ6VFBtJtDu09N-meigXTVsglPlF5GNw58nMuSk_sdJa47p9as7vIIoXJFblkv4vrnfTDe9T6_vQtJyoILXTH7NJih-dI8FPpqg42-E6T_jU-D67W-tpjwio5qycP4WowoZJ9-XmQ1P-EwWDTQk7BtHjRpCfLVfob5yMekpt5QkVqqvKcmo-C5oqgrZIcD4mElQIf37-FsB2qphf_GFuq1l5pRAULT-r8p0WlRodxWx5h-t8RmMAPuey5UdEeWM="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6216480554:AAExhwN0i7BFrm7WyTZerrLCMabo0Kg9Yqw"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001609539796
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
