# Crypto Blueprint
curl --request GET \
  --url http://localhost:5000/v1/crypto/usd/btc \
  --header 'content-type: application/json'

curl --request GET \
  --url http://localhost:5000/v1/crypto/usd/eth \
  --header 'content-type: application/json'

curl --request GET \
  --url http://localhost:5000/v1/crypto/eur/btc \
  --header 'content-type: application/json'

curl --request GET \
  --url http://localhost:5000/v1/crypto/eur/eth \
  --header 'content-type: application/json'

curl --request GET \
  --url http://localhost:5000/v1/crypto/usd/all \
  --header 'content-type: application/json'
curl --request GET \
  --url http://localhost:5000/v1/crypto/eur/all \
  --header 'content-type: application/json'

curl --request GET \
  --url http://localhost:5000/v1/crypto/trending \
  --header 'content-type: application/json'

# Cyber Blueprint
curl --request GET \
  --url http://localhost:5000/v1/cyber/cti/sources \
  --header 'content-type: application/json'
curl --request GET \
  --url http://localhost:5000/v1/cyber/cti/gov/sources \
  --header 'content-type: application/json'

# Economics Blueprint
curl --request GET \
  --url http://localhost:5000/v1/economics/sources \
  --header 'content-type: application/json'

curl --request GET \
  --url http://localhost:5000/v1/economics/gov/sources \
  --header 'content-type: application/json'

curl --request GET \
  --url http://localhost:5000/v1/economics/events \
  --header 'content-type: application/json'

curl --request GET  \
  --url http://localhost:5000/v1/economics/overview  \
  --header 'content-type: application/json'

curl --request GET  \
  --url http://localhost:5000/v1/economics/stocks/trending  \
  --header 'content-type: application/json'

curl --request GET  \
  --url http://localhost:5000/v1/economics/stocks/news  \
  --header 'content-type: application/json' 

# Scythe Blueprint
curl --request GET  \
  --url http://localhost:5000/v1/scythe/gov/contracts/latest  \
  --header 'content-type: application/json'

curl --request GET  \
  --url http://localhost:5000/v1/scythe/gov/contracts/aapl  \
  --header 'content-type: application/json'

curl --request GET  \
  --url http://localhost:5000/v1/scythe/corp/lobbying  \
  --header 'content-type: application/json'

curl --request GET  \
  --url http://localhost:5000/v1/scythe/gov/congress/trades \
  --header 'content-type: application/json'  

