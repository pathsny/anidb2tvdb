from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'Anidb to TheTVDB'
settings.subtitle = 'powered by web2py'
settings.author = 'Vishnu'
settings.author_email = 'pathsny@gmail.com'
settings.keywords = 'anidb, thetvdb'
settings.description = 'Provides information to map anidb ids to the related tvdb information.'
settings.layout_theme = 'RedCity'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = '03cf9fe9-4734-461b-ac1d-ba8fb0122e5b'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
