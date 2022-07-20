# Pulsar server standalone Tutorial
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

## Tenant, namespace, topic e schema
Executar comandos abaixo para criar o tenant, ns e topic: <b>persistent://rpa/ns01/tp01</b>

```bash
# entra no bash do conainer recursing_hermann criado acima:
docker exec -it recursing_hermann /bin/bash

# Criar o tenant "rpa", namespace "ns01" e topic "tp01" com schema definido em "/host/schema1_pulsa.json"
./bin/pulsar-admin tenants create rpa
./bin/pulsar-admin namespaces create rpa/ns01
./bin/pulsar-admin topics create rpa/ns01/tp01
./bin/pulsar-admin schemas upload --filename ./host/schema1_pulsa.json tp01

# grand permition
./bin/pulsar-admin topics grant-permission --actions produce,consume --role application1 persistent://rpa/ns01/tp01

# teste se sucesso
./bin/pulsar-admin namespaces list rpa
./bin/pulsar-admin topics list rpa/ns01
./bin/pulsar-admin topics permissions persistent://rpa/ns01/tp01
./bin/pulsar-admin schemas get tp01
```

## Fragmento decodigo python
```py
# ...
consumer = client.subscribe('persistent://rpa/ns01/tp01','test',schema=schema.StringSchema())
producer = client.create_producer('persistent://rpa/ns01/tp01',schema=schema.StringSchema())
# ...
```

## Status
Tenant: <b>persistent://rpa/ns01</b> ,topic: <b>tp01</b>
```bash
# api rest
curl http://localhost:8080/admin/v2/persistent/rpa/ns01/tp01/stats | python -m json.tool

```

refs:
- https://pulsar.apache.org/api/python/2.10.1/pulsar.html
- https://pulsar.apache.org/docs/next/client-libraries-python
- https://pulsar.apache.org/docs/next/concepts-messaging/#messages
- https://www.youtube.com/watch?v=KraWwiuSDkM&list=PL5SZre4MWFhuWu9ySy3H3ezyTbKYvs_t_&index=5&t=917s
- Conver schema field: https://tools.knowledgewalls.com/json-to-string