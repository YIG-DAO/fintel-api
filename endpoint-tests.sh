#!/bin/bash

# Define the base URL for your Flask app
BASE_URL="http://127.0.0.1:5000"

# Define the blueprints/endpoints you want to test
declare -a endpoints=(
    "/v1/crypto/usd/btc"
    "/v1/crypto/usd/eth"
    "/v1/crypto/eur/btc"
    "/v1/crypto/eur/eth"
    "/v1/crypto/usd/all"
    "/v1/crypto/eur/all"
    "/v1/crypto/trending"
    "/v1/cyber/cti/sources"
    "/v1/cyber/cti/gov/sources"
    "/v1/economics/sources"
    "/v1/economics/gov/sources"
    "/v1/economics/events"
    "/v1/economics/overview"
    "/v1/economics/stocks/trending"
    "/v1/economics/stocks/news"
    "/v1/scythe/gov/contracts/latest"
    "/v1/scythe/gov/contracts/aapl"
    "/v1/scythe/corp/lobbying"
    "/v1/scythe/gov/congress/trades"
)

# Iterate over each endpoint and use curl to make a request
for endpoint in "${endpoints[@]}"
do
    echo "Testing $BASE_URL$endpoint..."
    curl --request GET \
         --url "$BASE_URL$endpoint" \
         --header 'content-type: application/json'
    sleep 1 # Optional: sleep for a second between requests to space out logs
done

echo "Finished testing."