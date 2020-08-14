# Link Secrets and configmap into deployment

## Check the old output

```
kubectl exec -it tester -- curl mysvc
```

## Delete the old deployment

```
kubectl delete deployment k8s-ws
```

## Inspect the new deployment

```
cat k8s-ws.deployment.yaml
```

## Start the new deployment

```
kubectl create -f k8s-ws.deployment.yaml
```

## Check the new output

```
kubectl exec -it tester -- curl mysvc
```

## Check the situation within the pod

```
kubectl exec -it <k8s-ws pod name> -- sh
printenv | grep SECRET_LOG
ls -l /data
```

