# Pulsar server standalone Tutorial
Ajuste do venv e ativação do pulsar via docker-compose:
```bash
python3 -m venv venv
source ./venv/bin/activate

# Instalar dependencia python
pip3 install -r requirements.txt

# Ativar o servidor do docker-compose, e, entrar no mesmo
docker-compose up -d
docker exec -it pulsar-server /bin/bash

# Teste se ok
./bin/pulsar-admin functions-worker get-cluster
# {"workerId" : "c-standalone-fw-localhost-8080","workerHostname" : "localhost","port" : 8080}

exit
```

## Tenant, namespace, topic e schema  
Definição: <i>persistent://\<tenant>/\<namespace>/\<topic></i>
- <b>persistent://rpa/ns01/tp01</b> com schema <b>schema1_pulsa.json</b>.
    ```bash
    # Tenant "rpa", namespace "ns01" e topic "tp01" com schema definido por "schema1_pulsa.json"
    ./bin/pulsar-admin tenants create rpa
    ./bin/pulsar-admin namespaces create rpa/ns01
    ./bin/pulsar-admin topics create rpa/ns01/tp01
    ./bin/pulsar-admin schemas upload --filename ./host/schema1_pulsa.json tp01
    ./bin/pulsar-admin topics grant-permission --actions produce,consume --role application1 persistent://rpa/ns01/tp01

    # Lista definições acima
    ./bin/pulsar-admin namespaces list rpa
    ./bin/pulsar-admin topics list rpa/ns01
    ./bin/pulsar-admin topics permissions persistent://rpa/ns01/tp01
    ./bin/pulsar-admin schemas get tp01
    ```

- <b>persistent://rpa/ns01/topic-01</b> sem schema.
    ```bash
    # Tenant "rpa", namespace "ns01" e topic "topic-01" sem schema 
    ./bin/pulsar-admin topics create rpa/ns01/topic-01
    ./bin/pulsar-admin topics grant-permission --actions produce,consume --role application1 persistent://rpa/ns01/topic-01
    ```

## Consulta pulsar 
```bash
# Topico "tp01" com schemma
curl http://localhost:8080/admin/v2/persistent/rpa/ns01/tp01/stats | python3 -m json.tool

# Topico "topic-01" sem schemma
curl http://localhost:8080/admin/v2/persistent/rpa/ns01/topic-01/stats | python3 -m json.tool

# Generica
curl http://localhost:8080/admin/v2/persistent/public/default/my-topic/stats | python3 -m json.tool
```

refs:
- https://pulsar.apache.org/api/python/2.10.1/pulsar.html
- https://pulsar.apache.org/docs/next/client-libraries-python
- https://pulsar.apache.org/docs/next/concepts-messaging/#messages
- https://www.youtube.com/watch?v=KraWwiuSDkM&list=PL5SZre4MWFhuWu9ySy3H3ezyTbKYvs_t_&index=5&t=917s
- Conver schema field: https://tools.knowledgewalls.com/json-to-string