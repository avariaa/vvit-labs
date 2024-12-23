class UserAcccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password


    def set_password(self, new_password = input('Введите новый пароль:')):
        self.__password = new_password


    def check_password(self, password = input('Проверка пароля:')):
        return password == self.__password


user = UserAcccount('Варвара', 'vare4ka', '1230987')
user.set_password()
is_correct = user.check_password()
print(is_correct)