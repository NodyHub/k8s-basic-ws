# Link Secret in ENV 

## Check the updated deployment

```
cat yaml/deployment.k8s-ws.yaml
```

## Apply deployment

```
kubectl apply -f yaml/deployment.k8s-ws.yaml
```

## Check result

```
kubectl get pods
kubectl exec -it tester -- curl mysvc
```

