#!/usr/bin/env bash
set -euo pipefail

repo_root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
image_name="curs-scc-jenkins:lts"
container_name="curs-scc-jenkins"
jenkins_home_volume="curs_scc_jenkins_home"
docker_group_id=$(getent group docker | cut -d: -f3)

sudo docker build \
  -t "${image_name}" \
  -f "${repo_root}/jenkins/Dockerfile" \
  "${repo_root}"

sudo docker rm -f "${container_name}" >/dev/null 2>&1 || true

sudo docker run -d \
  --name "${container_name}" \
  --restart unless-stopped \
  --group-add "${docker_group_id}" \
  -p 8080:8080 \
  -p 50000:50000 \
  -v "${jenkins_home_volume}:/var/jenkins_home" \
  -v /var/run/docker.sock:/var/run/docker.sock \
  "${image_name}"

echo "Jenkins is starting on http://localhost:8080"
echo "When the setup wizard appears, the initial admin password is:"
echo "  sudo docker exec ${container_name} cat /var/jenkins_home/secrets/initialAdminPassword"