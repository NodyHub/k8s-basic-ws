# Secrets & ConfigMaps

## Create secret test logfile

```
for i in {1..9} ; do echo $(date +"%d/%m/%Y %H:%M:%S") Secrets from the cluster $i >> bar.log; done
```


## Create Secrets in the cluster

```
kubectl create secret generic logfiles --from-file=./bar.log
```

## Show Secrets

```
kubectl get secrets
kubectl describe secret logfiles
```

## Create ConfigMap

```
kubectl create configmap app-cfg --from-literal=secret_logfile_location=/data/bar.log
```

## Show ConfigMap
```
kubectl get configmap
kubectl describe configmap app-cfg
```
