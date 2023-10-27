#!/bin/bash

# Capture the start time
START_TIME=$(date +%s)

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
    # Perform the curl request and capture the output along with the timing and status
    OUTPUT=$(curl --silent \
                  --write-out "\nStatus: %{http_code}, Completed in %{time_total}s\n" \
                  --request GET \
                  --url "$BASE_URL$endpoint" \
                  --header 'content-type: application/json')
    
    # Extract the body of the response (everything before the last two lines)
    RESPONSE=$(echo "$OUTPUT" | head -n -2)
    
    # Try to extract the from_cache value using grep and awk
    FROM_CACHE=$(echo "$RESPONSE" | grep -o '"from_cache":[^,]*' | awk -F: '{print $2}' | tr -d ' ')

    # If jq couldn't find the from_cache key, it will return "null"
    if [ "$FROM_CACHE" != "null" ]; then
        echo "from_cache: $FROM_CACHE"
    else
        echo "from_cache key not found in response."
    fi

    # Print out the timing and status (last two lines of the output)
    echo "$OUTPUT" | tail -n 2
    sleep 1 # Optional: sleep for a second between requests to space out logs
done

# Capture the end time
END_TIME=$(date +%s)

# Calculate the time difference
TOTAL_TIME=$((END_TIME - START_TIME))

echo "Finished testing. Total time taken: $TOTAL_TIME seconds."