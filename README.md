simple api that calculate the similarity between 2 strings.

life is easy 
clone the repo 
type that on your terminal : 
docker-compose -f docker-compose.yml up -d --build

Example of a request:

http://localhost:port/api/calculateSimilarity/

	{
	"question":"I would love to go to the beach",
	"questions": [
		{"question":"I would like to have a sandwich","id":12},
		{"question":"This summer is so hot we gotta go to jump in a pool","id":12},
		{"question":"Lets go to the sea man","id":15}

		]
	}

