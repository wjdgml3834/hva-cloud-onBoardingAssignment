# build the docker image
docker build -t on_boarding_assignment .

# run the container
docker run -dp 3000:3000 on_boarding_assignment

