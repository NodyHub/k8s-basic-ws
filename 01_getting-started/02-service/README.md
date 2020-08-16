# Create Service

## List All

```
koubectl get all
```

## List Services

```
kubectl get service
kubectl get svc
```

## Expose Deployment	

```
kubectl expose deployment k8s-ws --name=mysvc --port 80 --target-port 5000
```

## List Services

```
kubectl get svc
```

## Create a "tester" pod and access the service

```
kubectl run tester --image=nodyd/k8s-ws
kubectl exec -it tester -- sh
ping -c1 mysvc
curl mysvc
curl mysvc:80
```

## inspect the IP addresses of the pod and the service

```
kubectl get all -o wide
```

## Change ServiceType ClusterIP-NodePort

```
kubectl patch svc mysvc --type='json' -p '[{"op":"replace","path":"/spec/type","value":"NodePort"}]'
```

## List Services and access the NodePort on the Host

```
kubectl get svc mysvc
minikube service --url mysvc
curl $(minikube service --url mysvc)
```
