# Environment 

## Inspect the new deployment

```
cat yaml/deployment.k8s-ws.yaml
```

## Apply new deployment

```
kubectl apply -f yaml/deployment.k8s-ws.yaml
```

## See whats happen

```
kubectl get pods
kubectl exec -it tester curl mysvc
```
