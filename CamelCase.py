print('Enter a sentence:')
UserSentence = input()
UserSentence = str(UserSentence)

UserSentence = UserSentence.title()
UserSentence = UserSentence.replace(" ", "")
UserSentence = UserSentence [:1].lower() + UserSentence[1:]

print (UserSentence)
