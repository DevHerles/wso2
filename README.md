
## Build Docker Image:
```sh
docker build -t hello-world-app .
```

## Test Locally:
```sh
docker run -d --name hello-world-container -p 8000:80 hello-world-app
```

## Deploy to Kubernetes:
```sh
kubectl apply -f ./k8s/api.yaml
```

