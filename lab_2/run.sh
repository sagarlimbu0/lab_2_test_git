python3 trainer/train.py

cp trainer/model_piepline.pkl .
cp trainer/features.pkl .

docker build -t lab_2_container .

docker run -d -p 8000:8000 lab_2_container
sleep 5.0

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

# docker stop lab_2_container

# docker images -f dangling=true