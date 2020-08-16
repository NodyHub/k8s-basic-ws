# Secrets & ConfigMaps

## ConfigMaps

### Create a new properties file 

```
cat << EOL > game.properties                    
enemies=aliens
lives=3
enemies.cheat=true
enemies.cheat.level=noGoodRotten
secret.code.passphrase=UUDDLRLRBABAS
secret.code.allowed=true
secret.code.lives=30
EOL

```

### Create ConfigMap

```
kubectl create configmap app-properties --from-file=game.properties
```

### Show ConfigMap
```
kubectl get configmap
kubectl describe configmap app-properties
```

## Secrets

### Create Secrets in the cluster

```
kubectl create secret generic app-cfg --from-literal=con-string=mongodb://mongo:superSecretMongoPw@mongodb-injected-secret
```

### Show Secrets

```
kubectl get secrets
kubectl describe secret app-cfg
```
