class DevelopmentConfig():
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='Alex'
    MYSQL_PASSWORD='A123'
    MYSQL_DB='api_utl'
    MYSQL_CURSORCLASS='Cursor'

config={
    'development': DevelopmentConfig
}