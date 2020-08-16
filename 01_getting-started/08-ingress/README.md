# Ingress

## Prepare Minikube

```
minikube addons enable ingress
```

## Create generic ingress

```
kubectl create -f yaml/ingress.k8s-ws.v1.yaml
```

## Test ingress from host 

```
kubectl get ingress k8s-ws
curl <ip of ingress>
```

## Create an additional service

```
kubectl create deployment hello --image=nodyd/hello
kubectl expose deployment hello --name=hello --port 80 --target-port 80
```

## Test

```
kubectl exec -it tester -- curl hello
```

## Apply the updated Ingress

```
kubectl apply -f yaml/ingress.k8s-ws.v2.yaml
```

## Test ingress from host

```
kubectl get ingress k8s-ws
curl <ip of ingress>
curl <ip of ingress>/hello
```


## Create an additional service
```
kubectl create deployment google-hello --image=gcr.io/google-samples/hello-app:1.0
kubectl expose deployment google-hello --name=ghello --port 80 --target-port 80
```

## Test

```
kubectl exec -it tester -- curl ghello
```

## Apply the updated Ingress

```
kubectl apply -f yaml/ingress.k8s-ws.v3.yaml
```

## Test ingress from host

```
kubectl get ingress k8s-ws
curl <ip of ingress>
curl <ip of ingress>/hello
curl -H "Host: foobar" <ip of ingress>
```
