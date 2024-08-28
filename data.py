class ApiUrls:
    HOME_URL = 'https://stellarburgers.nomoreparties.site/'
    LOGIN = f'{HOME_URL}login'
    FORGOT_PASS = f'{HOME_URL}forgot-password'
    RESTORE_PASS = f'{HOME_URL}reset-password'
    CREATE_USER = f'{HOME_URL}api/auth/register'
    DELETE_USER = f'{HOME_URL}api/auth/user'
    PROFILE = f'{HOME_URL}account/profile'
    ORDER_HISTORY = f'{HOME_URL}account/order-history'
    ORDER_FEED = f'{HOME_URL}feed'


class ExistingUser:
    email = "300@ya.ru"
    password = "123456"
    name = "Test1User"
