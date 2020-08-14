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
kubectl get all
```

## Inspect the `*.yaml` files

```
ls -l yaml/
cat yaml/k8s-ws.deployment.yaml
cat yaml/tester.pod.yaml
cat yaml/mysvc.svc.yaml
cat yaml/logfiles.secrets.yaml
```

## Create the resources with the yaml files

```
kubectl create -f yaml/k8s-ws.deployment.yaml
kubectl create -f yaml/tester.pod.yaml
kubectl create -f yaml/mysvc.svc.yaml
kubectl create -f yaml/logfiles.secrets.yaml
```

## See that everything is back

```
kubectl get all
```
