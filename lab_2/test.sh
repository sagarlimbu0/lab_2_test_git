curl -X POST -H 'Content-Type: application/json' localhost:8000/predict -d \
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
	
	# curl -X POST -H 'Content-Type: application/json' localhost:8000/predict -d \
	# '[
	#     {"MedInc":45.0, 
	#     "HouseAge":25.4, 
	#     "AveRooms":40.0, 
	#     "AveBedrms":5.8, 
	#     "Population":450.0, 
	#     "AveOccup":2.5, 
	#     "Latitude":30.86, 
	#     "Longitude": -122.25}
	# ]'
	
	# curl -X POST -H 'Content-Type: application/json' localhost:8000/predict -d \
	# '[
	#     {"MedInc":1,
	#     "HouseAge":41.0,
	#     "AveRooms":6.984127,
	#     "AveBedrms":1.023810,
	#     "Population":322.0,
	#     "AveOccup":2.555556,
	#     "Latitude":37.88,
	#     "Longitude": -122.22}
	# ]'
	
	# curl -X POST -H 'Content-Type: application/json' localhost:8000/predict -d \
	# '[
	#     {"MedInc":5.6431,
	#     "HouseAge":52.0,
	#     "AveRooms":5.817352,
	#     "AveBedrms":1.081081,
	#     "Population":558.0,
	#     "AveOccup":2.547945,
	#     "Latitude":37.85,
	#     "Longitude":-122.25}
	# ]'
	
	# curl -X POST -H 'Content-Type: application/json' localhost:8000/predict -d \
	# '[
	#     {"MedInc":3.8462,
	#     "HouseAge":52.0,
	#     "AveRooms":6.281853,
	#     "AveBedrms":1.081081,
	#     "Population":565.0,
	#     "AveOccup":2.181467,
	#     "Latitude":37.85,
	#     "Longitude":-122.25}
	# ]'
	
