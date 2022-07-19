# Pulsar server standalone
Ajuste do venv e ativação do pulsar via docker:
```bash
python3 -m venv venv
source ./venv/bin/activate

# Instalar dependencia wheel
pip3 install install pulsar-client

# Docker servidor standalone de teste
docker run -it -p 6650:6650 \
           -p 8080:8080 \
           --mount source=pulsardata,target=/pulsar/data \
           --mount source=pulsarconf,target=/pulsar/conf \
           apachepulsar/pulsar:2.9.1 \
           bin/pulsar \
           standalone

# entra no bash do conainer recursing_hermann criado acima:
docker exec -it recursing_hermann /bin/bash

# verificar se esta ok
./bin/pulsar-admin functions-worker get-cluster
# {"workerId" : "c-standalone-fw-localhost-8080","workerHostname" : "localhost","port" : 8080}

exit

# consulta default (sem teanet e namespace)
curl http://localhost:8080/admin/v2/persistent/public/default/my-topic/stats | python -m json.tool
```

# Tenants e namespacecs
Executar comando para criar o tenant: <b>persistent://rpa/ns01</b>

```bash
# entra no bash do conainer recursing_hermann criado acima:
docker exec -it recursing_hermann /bin/bash

# Criar o tenant "rpa" com namespace "ns01"
./bin/pulsar-admin tenants create rpa
./bin/pulsar-admin namespaces create rpa/ns01

# teste se sucesso
./bin/pulsar-admin namespaces list rpa

# Criar topico tp01 em tenant rpa, namespace ns01 
./bin/pulsar-admin topics create rpa/ns01/tp01

# Listar topicos
./bin/pulsar-admin topics list rpa/ns01

# Listar seguranca
./bin/pulsar-admin topics permissions persistent://rpa/ns01/tp01

# grand permition
./bin/pulsar-admin topics grant-permission --actions produce,consume --role application1 persistent://rpa/ns01/tp01


# upload do schema (texto)
./bin/pulsar-admin schemas upload --filename ./host/aa.json tp01
./bin/pulsar-admin schemas get tp01

```

## Fragmento decodigo python
```py
# ...
consumer = client.subscribe('persistent://rpa/ns01/topicA','test',schema=schema.StringSchema())
producer = client.create_producer('persistent://rpa/ns01/topicA',schema=schema.StringSchema())
# ...
```

## Status
Tenant: <b>persistent://rpa/ns01</b> 
```bash
# api rest
curl http://localhost:8080/admin/v2/persistent/rpa/ns01/topicA/stats | python -m json.tool

```

refs:
- https://pulsar.apache.org/api/python/2.10.1/pulsar.html
- https://pulsar.apache.org/docs/next/client-libraries-python
- https://pulsar.apache.org/docs/next/concepts-messaging/#messages