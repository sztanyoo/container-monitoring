/bin/sed -e 's@~SLACK_URL~@'"${slack_url}"'@' /slack-notify.yaml > /etc/grafana/provisioning/notifiers/slack-notify.yml
/run.sh