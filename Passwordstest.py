passwords = ["about", "after", "again", "below", "could", 
             "every", "first", "found", "great", "house", 
             "large", "learn", "never", "other", "place",
             "plant", "point", "right", "small", "sound",
             "spell", "still", "study", "their", "there",
             "these", "thing", "think", "three", "water",
             "where", "which", "world", "would", "write"]
z = passwords
x = []
a=['h','g','p','n','v','o']
b=['r','k','f','b','n','t']
c=['j','p','s','b','h','l']
d=['t','e','z','j','q','w']
e=['i','a','j','d','s','r']

for i in z:
	if i[0] in a:
		x.append(i)

print(x)
