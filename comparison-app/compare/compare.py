from products import ageas
import json

def lambda_handler(event, context):
	# comparison using a loop and a list
	# set the list up to set variables for everything in the product algs
	comparelist = [ageas]


	# from the comparelist, set the first field to the default cheapest and decline values
	cheapest = comparelist[0].insurerdict

	# Create the blank decline list, ready for population with decline info
	declinelist = []
	quotelist = []

# loop for identifying the cheapest price and updating (cheapest) with the insurerdict field

	for insurer in comparelist:
		if insurer.insurerdict["price"] < cheapest["price"]and insurer.insurerdict["price"] != 0:
			cheapest = insurer.insurerdict #this bit populates (cheapest) with the info from insurerdict from the cheapest insurer

# the if's are in line as they are run separately
		if insurer.insurerdict["decline"] != "":
			decline = insurer.insurerdict #this bit populates (decline) with the info from any insurerdict which contains "decline" info
			declinelist.append(decline) #this bit adds the decline info for that insurer in to the declinelist

		if insurer.insurerdict["price"] != 0 and insurer.insurerdict["price"] != 99999:
			quote = insurer.insurerdict
			quotelist.append(quote)


	for insurer in declinelist: #for any insurer in the declinelist, output the name and the reason
		print("Unfortunately " + insurer["name"] + " has declined your quote as it is " + insurer["decline"])

	print("The following insurers have offered you a quote: ")
	for insurer in quotelist:
		print(insurer["name"])

# print the output
	print("Your cheapest price is £" + str(cheapest["price"]) + " with " + cheapest["name"])

	return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Your cheapest price is &#163;" + str(cheapest["price"]) + " with " + cheapest["name"],
        }),
    }