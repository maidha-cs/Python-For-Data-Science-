def welcome_user(username, city="Pakistan"):
    message = f"Assalam-o-Alaikum {username}! Welcome to our Data Science track from {city}."
    return message
user1 = welcome_user("Maidha Fatima", "Karachi")
print(user1)
user2 = welcome_user("Shariq Khan")
print(user2)