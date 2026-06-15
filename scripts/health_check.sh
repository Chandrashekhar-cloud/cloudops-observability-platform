#!/bin/bash

echo "Checking services..."

curl -s http://localhost:5000/health && echo " Flask OK"
curl -s http://localhost:9090/-/healthy && echo " Prometheus OK"
curl -s http://localhost:9093/-/healthy && echo " Alertmanager OK"
curl -s http://localhost:3100/ready && echo " Loki OK"
curl -s http://localhost:3000/api/health && echo " Grafana OK"
