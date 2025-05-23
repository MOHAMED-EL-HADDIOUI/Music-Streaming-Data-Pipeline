## Eventsim

This is a modified version of the eventsim project. The docker image is based on a maintained fork of the original project.

### Setup

#### Docker Image
```bash
docker build -t events:1.0 .
```

#### Run With Kafka Configured On Localhost
```bash
docker run -it \
  --network host \
  events:1.0 \
    -c "examples/example-config.json" \
    --start-time "`date +"%Y-%m-%dT%H:%M:%S"`" \
    --end-time "2022-03-18T17:00:00" --nusers 20000 \
    --kafkaBrokerList localhost:9092 \
    --continuous
```