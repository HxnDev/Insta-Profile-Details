from instagramy import InstagramUser

# Can be installed by running "pip install instagramy" on terminal

username = input("Enter the insta username of the person = ")

user = InstagramUser(username)
bio = user.biography
print("Bio = ", bio)

followers = user.number_of_followers
print("Total Followers = ", followers)

following = user.number_of_followings
print("Total Followings = ", following)

posts = user.number_of_posts
print("Total posts = ", posts)
