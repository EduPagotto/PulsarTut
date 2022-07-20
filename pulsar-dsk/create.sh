#!/bin/bash
./bin/pulsar-admin tenants create rpa
./bin/pulsar-admin namespaces create rpa/ns01
./bin/pulsar-admin topics create rpa/ns01/tp01
./bin/pulsar-admin topics grant-permission --actions produce,consume --role application1 persistent://rpa/ns01/tp01
./bin/pulsar-admin schemas upload --filename ./host/schema1_pulsa.json tp01
