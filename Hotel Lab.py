# Hotel Lab.py

#Vanessa Crighton

#This program determines the cost of a hotel stay to include meals and excursions.





#define room costs
n =0
rt = 0
rp = 0
nop = 0

def rc(n, rt):
	if rt == 1: #one king bed
		rc = (n * 350)
		return rc
	elif rt == 2:
		rc = (n * 375)
		return rc
	elif rt == 3: 
		rc = (n * 475)
		return rc
	elif rt == 4: 
		rc = (n * 525)
		return rc

#define meal cost
mc = 0
nb = 0
tip = 0
tm = 0
nd = 0

def mc(nb, nd):
	mc = ((nb * 25) + (nd * 75))
	tip = (mc * 0.15)
	tm = (tip + mc)
	return tm



#excursions
tec = 0
pc = 0
sk = 0
gh = 0
bd = 0

def tec(pc, sk, gh, bd, nop):
	tec = 0
	if pc == "y":
		tec = (tec + 50)
	if sk == "y":
		tec = (tec + (25 * nop))
	if gh == "y":
		tec = (tec + (17 * nop))
	if bd == "y":
		tec = (tec + 200)
	return tec
	
#inputs
n = int(input("Number of Nights: "))
nop = int(input("Number of Guests: "))
#rooms
print("Room Types:")
print("(1) - One King Bed ($350/night)")
print("(2) - Two Queen Beds ($375/night)")
print("(3) - King Suite ($475/night)")
print("(4) - Queen Suite ($525/night)")
rt = int(input("Choose Room Type: "))
#meals
print("Brunch: $25")
print("Dinner: $75")
print("* 15% gratuity will be added automatically *")
nb = int(input("Number of Brunches: "))
nd = int(input("Number of Dinners: "))
#Excursions
print("Excursions: ")
print("Picnic: $50")
print("Snorkeling: $25 per person")
print("Guided Hike: $17 per person")
print("Boat Dinner (for 2): $200")
pc = input("Would you like to go on a picnic? [y/n]: ")
sk = input("Would you like to go snorkeling? [y/n]: ")
gh = input("Would you like to go on a guided hike? [y/n]: ")
bd = input("Would you like to have dinner on a boat? [y/n]: ")

#bill
print("Summary of Charges")
tr = rc(n, rt)
print("Room: ", tr)
fmc = (mc (nb, nd) * nop)
print("Meals: ", fmc)
fec = tec(pc, sk, gh, bd, nop)
print("Excursions: ", fec)
gt = tr + fmc + fec
print("Total Amount: ", gt)
