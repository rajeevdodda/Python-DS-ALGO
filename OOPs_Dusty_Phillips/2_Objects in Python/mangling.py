class SecretString:
    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase

    def decrypt(self, pass_phrase):
        if pass_phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return ""


secret_string = SecretString("rahul", "rajeev")
print(secret_string.decrypt("rajeev"))
try:
    print(secret_string.__plain_string)
except AttributeError as error:
    print(error)

print(dir(secret_string))
print(secret_string._SecretString__plain_string)
