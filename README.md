# python-jaeger-tracing
Implementando tracing com Jaeger, criando uma aplicação com dois serviços Python que se comunicam via HTTP, configurando o Jaeger para rastrear as requisições entre os serviços e visualizando os traces no painel do Jaeger.

# Instalação do WSL
Realizei a instalação do WSL conforme descrito [neste guia](https://github.com/codeedu/wsl2-docker-quickstart).

# Pré-requisitos : 
- Python 3.10.12
- pip 22.0.2
- Docker 28.1.1

# Como executar : 

1 - Iniciei o Jaeger com Docker fazendo o serviço de rastreamento rodar na
máquina local :

```bash
docker run -d --name jaeger \
  -e COLLECTOR_OTLP_ENABLED=true \
  -p 6831:6831/udp \
  -p 6832:6832/udp \
  -p 5778:5778 \
  -p 16686:16686 \
  -p 4317:4317 \
  -p 4318:4318 \
  -p 14250:14250 \
  -p 14268:14268 \
  -p 14269:14269 \
  -p 9411:9411 \
  jaegertracing/all-in-one:latest
```
2 - Depois de executei e acessei o Jaeger em:
```bash
http://localhost:16686
```
3 - # Instalei as depências : 
```bash
pip install flask requests opentelemetry-sdk opentelemetry-exporter-otlp
opentelemetry-instrumentation-flask opentelemetry-instrumentation-requests
```
4 - Realizei a instrumentação de serviços com o “OpenTelemetry” para enviar dados de
rastreamento para o Jaeger para o arquivo “service1.py” e “service2.py” já codificados nos arquivos

5 - Após isso configurado acessei meu “Jeager UI” e fiz a verificação das requisições
service1 e service2 :

https://github.com/user-attachments/assets/c7c3f4e6-d1e9-43a1-8ec3-b57715e61f45
