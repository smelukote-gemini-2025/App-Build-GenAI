![alt text](image.png)
![alt text](image-2.png)
![alt text](image-3.png)
![alt text](image-4.png)
![alt text](image-5.png)
![alt text](image-6.png)
![alt text](image-7.png)

gcloud run deploy frontend \
    --image gcr.io/cs-poc-lhsovao7bcucdrmgyhgjrvg/frontend-service-image \
    --platform managed \
    --region us-west1 \
    --allow-unauthenticated \
    --set-env-vars RETRIEVAL_SERVICE_URL="https://YOUR_RETRIEVAL_SERVICE_URL.run.app"

![alt text](image-8.png)
