# k8s

### kubectl and k3d
```
$ brew install kubectl k3d
$ k3d create --server-arg --no-deploy --server-arg traefik
$ export KUBECONFIG="$(k3d get-kubeconfig --name='k3s-default')"
$ kubectl cluster-info
```

### kubectl command
```
$ cd python-sample
$ kubectl apply -f configmap.yaml
$ kubectl get configmap python-sample -o yaml
$ kubectl apply -f deployments.yaml
$ kubectl get pod
$ kubectl apply -f service.yaml
$ kubectl get svc
$ kubectl port-forward svc/python-sample 8080:80
```
```
$ cd java-sample
$ kubectl apply -f configmap.yaml
$ kubectl get configmap java-sample -o yaml
$ kubectl apply -f role.yaml
$ kubectl apply -f deployments.yaml
$ kubectl get pod
$ kubectl apply -f service.yaml
$ kubectl get svc
$ kubectl port-forward svc/java-sample 8080:80
```

### cleanup
$ k3d delete
