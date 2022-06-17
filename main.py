# We are going to calculate the total cost of videos rented at Five Star Retro Video based on what types of videos are being rented:

# Input the number of new videos being rented by a customer
newVideosString = input("How many new videos is the customer renting? ")
newVideos = int(newVideosString)

# Compute the total cost of the number of new videos being rented using the formula:
# New video cost = 3.00 * number of new videos
newVideoCost = 3.00 * newVideos

# Input the number of oldies videos being rented by a customer
oldiesVideosString = input("How many oldies videos is the customer renting? ")
oldiesVideos = int(oldiesVideosString)

# Compute the total cost of the number of oldies videos being rented using the formula:
# Oldies video cost = 2.00 * number of oldies videos
oldiesVideoCost = 2.00 * oldiesVideos

# Compute the total cost of the rentals using the formula:
# Total rental cost = New video cost + Oldies vide cost
totalRentalCost = newVideoCost + oldiesVideoCost
float(totalRentalCost)
# Print the total rental cost
print("The total cost of the customer's rentals is $" + str(totalRentalCost) + "0.")