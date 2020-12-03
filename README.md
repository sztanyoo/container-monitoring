Container-monitoring
====================

This is a sample application monitored by Prometheus and visualized on Grafana

Dependencies
------------
- Docker
- Docker-compose

Usage
-----

Clone the repo first. If you need slack notifications, then set `services.grafana.environment.slack_url` in `docker-compose.yml`. Then start the application using `docker-compose`
```
$ docker-compose -f docker-compose.yml up
```

A sample application is available on http://localhost:9092/. It exposes the application related metrics (some random-like numbers) on http://localhost:9092/metrics

Prometheus is available on http://localhost:9090/. One can check the `login_time` and `transaction_count` metrics. Since the latter is a continuously increasing number, it makes sense monitoring it's change rate like `rate(transaction_count[1m])`.

Grafana is exposed on http://localhost:9091/. Default access is `admin`/`admin`. One might want to add Prometheus datasource and create dashboards/alerts.