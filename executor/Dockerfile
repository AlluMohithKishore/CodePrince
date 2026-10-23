FROM ubuntu:24.04
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends gcc g++ openjdk-21-jdk-headless python3 golang-go && useradd -m -u 10001 runner && rm -rf /var/lib/apt/lists/*
USER runner
WORKDIR /work
ENTRYPOINT ["/bin/sh", "-c"]
