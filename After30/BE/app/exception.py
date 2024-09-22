from fastapi import HTTPException, status


class Duplicated_User(Exception):
    def __init__(self):
        self.message = "Duplicated User"
        self.status_code = status.HTTP_400_BAD_REQUEST
