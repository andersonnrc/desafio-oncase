# desafio-oncase

Desafio proposto pela empresa Oncase para o desenvolvimento de um processo de web crawling para estruturar dados de portais concorrentes de notícias, agregar métricas sobre esses dados e disponibilizar informações..

## Informações sobre o projeto

O tema escolhido para esta solução foi sobre motos. Portanto os portais utilizados para a captura de informações foram:

* [Motoo](https://www.motoo.com.br/)
* [MotoTour](https://mototour.com.br/)
* [TudodeMotos](https://tudodemotos.com.br/)

## Tecnologias utilizadas

* Python 3.8
* Scrapy
* Docker
* MongoDB
* MongoDB Compass
* SO: Linux

## Build da aplicação

1. Criar instância do MongoDB pelo Docker

```
docker run -d --name mongodb -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=mongoadmin mongo
```

Pode-se utilizar qualquer ferramenta client para acessar o MongoDB para criar um database e uma collection. Para o desafio foi utilizado o [MongoDB Compass](https://www.mongodb.com/products/compass)

Então, após instalar a ferramenta client será necessário configurar a string de conexão a seguir:

```
mongodb://admin:mongoadmin@localhost:27017
```

Após conectar no MongoDB será necessário criar um database com o nome "test" e uma collection com o nome "portaismotos"

2. Clonar repositorio do projeto na máquina local

```
git clone https://github.com/andersonnrc/desafio-oncase.git
```

3. Instalação de pacotes

Via terminal, após clonar o repositório basta acessar o diretório desafio-oncase e digitar:

```
pip install -r requirements.txt
```

4. Executar aplicação

Ainda no terminal, basta digitar o comando a seguir:

```
./start.sh
```

## Dados obtidos

Nos três portais não seção relacionada a comentários de usuários ou likes, então não foi possível obter dados sobre engajamento.

A única exceção sobre algum dado possível de ser coletado sobre engajamento é o portal Tudo de Motos, que possui uma área no site sobre postagens no Twitter, então com um algortimo mais elaborado poderia ser analisado a quantidade de likes, retweets e comentários sobre as postagens.

Os dados obtidos foram:

- título da notícia
- autor da postagem
- data da postagem 
- tags
- texto da notícia
- link
- tags
- inclusão de um campo "site" para identificar a qual portal o documento do MongoDB se refere

O MotoTour foi o único portal o qual não se utiliza de tags nas notícias.

## Sugestões para Análises

1. Análise de sentimentos através de nuvem de palavras a partir dos textos e das tags e das notícias. Em uma situação onde os portais estão conectados às redes sociais, seria possível analisar o grau de frequência das palavras das notícias e que foi postada nas redes, assim poderia haver um estudo mais aprofundado e identificar quais palavras trazem maior engajamento nas postagens a partir de likes, retweets e postagens, etc.

2. Algum tipo de ranking, podendo ser um gráfico de barras ou pizza, para exibir a frequência em que esses portais postam notícias, como quantidade de notícias diárias, semanais, mensais.

3. Verificar quem são os autores das postagens dos respectivos portais e quem possui maior número de postagens podendo fazer análise semana, mensal, etc.

## Monitoramento dos web crawlers

Existe um projeto disponibilizado no GitHub chamado [SpiderKeeper](https://github.com/DormyMo/SpiderKeeper) o qual permite gerenciar os web crawlers a partir de um painel, além de permitir programar a execução automática como também mostrar estatísticas de execução.

## Escalabilidade da aplicação

Para o cenário do desafio, o consumo de recursos computacionais é baixo. Entretanto em uma situação hipotética o qual necessite de algumas centenas de web crawlers em execução, é interessante utilizar uma máquina em cloud para poder escalar aumentando os recursos computacionais. Um bom exemplo de solução para colocar os web crawlers é o [Amazon EC2](https://aws.amazon.com/pt/ec2/) e para armazenamento de dados existem duas opções também na Amazon, o [Amazon DynamoDB](https://aws.amazon.com/pt/dynamodb/features/) que suporta bancos de dados com o modelo de documentos e o [Amazon DocumentDB](https://aws.amazon.com/pt/documentdb/?c=db&sec=srv) que possui compatibilidade com o MongoDB.

## Funcionalidades pendentes e bugs a serem resolvidos

Para a carga incremental a mesma não foi implementada até o momento. Então a solução de contorno utilizada na execução foi incluir uma instrução no arquivo start.sh que exclui todos os documentos armazenados no MongoDB, sendo assim necessário fazer o processo de web scraping em todos os portais novamente.

O processo de web scraping no Motoo foi aparentemente mais fácil de percorrer todas as páginas e captar dados de todas as notícias, entretanto os outros dois estão apresentando problemas no código. O web crawler do MotoTour apesar de percorrer todas as páginas, não consegue captar todas as notícias e o portal TudodeMotos por apresentar várias seções de notícia no seu portal, tive que implementar o web crawler para rastrer as notícias a partir da segunda página.

### Contato

[Linkedin](https://www.linkedin.com/in/anderson-ribeiro-carvalho)


