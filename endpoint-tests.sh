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
  --url http://localhost:5000/v1/cyber/cti/sources \
  --header 'content-type: application/json'
curl --request GET \
  --url http://localhost:5000/v1/cyber/cti/gov/sources \
  --header 'content-type: application/json'

curl --request GET \
  --url http://localhost:5000/v1/economics/sources \
  --header 'content-type: application/json'

curl --request GET \
  --url http://localhost:5000/v1/economics/gov/sources \
  --header 'content-type: application/json'
