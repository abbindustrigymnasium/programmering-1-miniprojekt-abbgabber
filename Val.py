from Partier import Partier
import numpy

maxröster = 1
stop = False

förnamn = ["Karl","Nils","Mikael","Bo","Christer","Björn","Erik","Daniel","Anton"]
efternamn = ["Johansson","Svensson","Pettersson","Petersson","Lindström","Lindqvist","Danielsson"]
namn = []

    for parti in Partier:
            röster = numpy.random.randint(low = parti["min_röst"], high = parti["max_röst"])
            maxröster += röster
            # print (parti["namn"], ":" , röster)
            # print(maxröster)
            parti["resultat"]= röster
    if maxröster <= 100:
        for parti in Partier:
            print(parti["namn"], ":", parti["resultat"])
        stop = True
        print(maxröster)
    else:
        maxröster = 0
        
        # Räknar ut hur många röster alla partier fick och lägger in de i en dictionary
        # Om det blir mer än 100% röster så gör den om det
