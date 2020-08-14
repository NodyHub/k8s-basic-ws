# Create and handle Yaml Files

## List Resources

```
kubectl get all
```

## Get Yaml output of resources

```
kubectl get deployment k8s-ws -o yaml
kubectl get deployment mysvc -o yaml
```

## Delete all resources

```
kubectl delete svc mysvc
kubectl delete deployment k8s-ws
kubectl delete pod tester
```

## Inspect the `*.yaml` files

```
ls -l *.yaml
cat k8s-ws.deployment.yaml
cat tester.pod.yaml
cat mysvc.svc.yaml
cat secret
```

