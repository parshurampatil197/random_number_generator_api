Write a random no generator.

- Provide an API which generates a random no for a given URL.
- The random no must be saved in the redis NoSQL database.
- If the same URL is sent again, don't generate a new number, instead return the one previously generated and saved in Redis.
- Every time the random no is generated, push that number as a message to kafka.
- Kafka consumers should read the number and save it in the file with URL mapping.

e.g. 
1. User makes an API call with youtube.com, the API returns a random number say 10023.
2. User makes an API call with liverpoolfc.com  API returns a random number say 98345.
3. User again makes an API call with youtube.com and the server returns 10023 previously returned in step 1
4. Kafka consumer saves following mapping in the file

youtube.com 10023
liverpoolfc.com 98345

Please ensure to use Django for the API server, Add an api in user-api which will push msg in kafka, and in the dataprocessor that msg will be consumed and processed.
