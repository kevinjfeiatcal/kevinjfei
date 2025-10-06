# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?

def names(dictionary):
	for key in dictionary:
		print(key)

def namesandtype(dictionary):
	for name, info in dictionary.items():
		print(f"{name}: {info["Spectral Type"]}")


def brightstars(dictionary):
	for name, info in dictionary.items():
		if info["Magnitude"] > 0.1:
			print(f"{name}: {info["Magnitude"]}")

def addTarget(dictionary, name, RA, Dec, Magnitude, SpectralType):
	dictionary[name] = {
		"RA": RA,
		"Dec": Dec,
		"Magnitude": Magnitude,
		"Spectral Type": SpectralType
	}

def finddegree(dec):
		deg = float(dec.replace("°", "").split("°")[0].replace("+", ""))
		return deg

def brightesttwenty(dictionary):
	closest_star = None
	closest_diff = float("inf")
	for name, info in dictionary.items():
		dec = info["Dec"]
		diff = abs(finddegree(dec)-20)
		if diff < closest_diff:
			closest_diff = diff
			closest_star = name
	print(f"The star closest to twenty degrees is: {closest_star}.")
