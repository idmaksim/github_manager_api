from github import Github

# Замените 'your_username' и 'your_password' на ваши учетные данные GitHub
g = Github(login_or_token='Bopleromn', password='7403439Mv')

# Получение вашего аккаунта
user = g.get_user()

print(user.name)


#  Генерация нового токена
# new_token = user.create_authorization(
#     scopes=['repo'],
#     note="Generated token for Python script"
# )

# # Вывод срированного токена
# print("Your generated token is:", new_token.token)