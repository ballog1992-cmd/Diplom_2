class DataTestloginUser:

    email = "wrong_email_12345@test.ru"
    password = "wrong_password_999"


class DataCode:

    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409
    

class DataMasseage:

    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    BAD_REQUEST_MESSEAGE = "Ingredient ids must be provided"
    UNAUTHORIZED_MASSEAGE = "email or password are incorrect"
    UNAUTHORIZED_MASSEAGE_ORDER = "You should be autorised"

    FORBIDDEN_FIELD = "Email, password and name are required fields"
    FORBIDDEN_DUBLICATE = "User already exists"
    NOT_FOUND = 404
    CONFLICT = 409
    