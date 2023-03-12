#!/bin/bash
IMAGE_NAME= lab_2_container
APP_NAME= lab_2

python3 trainer/train.py

cp trainer/model_piepline.pkl .
cp trainer/features.pkl .

# Run pytest
poetry env remove python3.10
poetry install
poetry run pytest -vv -s

# stop previous image
# docker stop ${APP_NAME}
# docker rm ${APP_NAME}

# re-build image
docker build -t ${IMAGE_NAME} .
docker run -d --name ${APP_NAME} -p 8000:8000 ${IMAGE_NAME}

sleep 5.0

# health condition
# finished=false
# while ! $finished; do
#     health_status=$(curl -o /dev/null -s -w "%{http_code}\n" -X GET "http://localhost:8000/health")
#     if [ ($health_status) ]; then
#         finished=true
#         echo "API is ready"
#     else
#         echo "API not responding yet"
#         sleep 1
#     fi
# done

echo "testing '/hello' endpoint with ?name=Winegar"
curl -o /dev/null -s -w "%{http_code}\n" -X GET "http://localhost:8000/hello?name=Winegar"

echo "testing '/' endpoint"
curl -o /dev/null -s -w "%{http_code}\n" -X GET "http://localhost:8000/"

echo "testing '/docs' endpoint"
curl -o /dev/null -s -w "%{http_code}\n" -X GET "http://localhost:8000/docs"

echo "testing '/predict' endpoint"
curl -o /dev/null -s -w "%{http_code}\n" -X POST -H 'Content-Type: application/json' localhost:8000/predict -d \
'[
    {"MedInc": 22.0,
    "HouseAge": 33.4,
    "AveRooms": 40.0,
    "AveBedrms": 5.8,
    "Population": 322.0,
    "AveOccup": 2.5,
    "Latitude": 37.86,
    "Longitude": -122.25
    }
]'

echo "testing '/health' endpoint"
curl -o /dev/null -s -w "%{http_code}\n" -X GET "http://localhost:8000/health"

docker logs ${APP_NAME}

docker stop ${APP_NAME}
docker rm ${APP_NAME}

# delete the built image
docker image rm ${APP_NAME}
