# pip install instabot

from instabot import Bot
bot=Bot()

bot.login(username="username",password="password")

# bot.upload_photo("C:/Users/akash2001/Desktop/image.jpg",caption="Caption")
# bot.follow("username")
# bot.send_message("Hello!",['user1','user2'])
# bot.unfollow("username")
# bot.logout()

# bot.like("username")
# bot.unlike("username")
# bot.get_user_info("username")
# bot.get_user_following("username")
#bot.get_user_followers("username")

##list all followers of a user
followers=bot.get_user_followers("username")
for follower in followers:
    print(bot.get_user_info(follower))


# ## Search a name's part by user inout and list all the users with that name otherwise showing no username matched with user input string
# search_query = input("Enter the part of the username to search: ")
# matched_users = []

# all_users = bot.get_user_following("username")  # Assuming you want to search within the following list
# for user in all_users:
#     user_info = bot.get_user_info(user)
#     if search_query.lower() in user_info['username'].lower():
#         matched_users.append(user_info['username'])

# if matched_users:
#     print("Matched usernames:")
#     for user in matched_users:
#         print(user)
# else:
#     print("No username matched with the input string.")