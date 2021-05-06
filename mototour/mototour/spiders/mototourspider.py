import scrapy
from ..items import MototourItem

class MototourSpider(scrapy.Spider):
    
    name = "mototour-crawler"
    
    start_urls = ['https://mototour.com.br/news/pag/1']
    
    def parse(self, response):
        
        #conteudo = response.css('div.textos_com_foto')
        conteudo = response.css('div#dv-palco')
        
        for campos in conteudo:    
            link = campos.css('p.titulo3 a::attr(href)').extract_first()
            
            yield response.follow(link, self.parse_conteudo)
   
            proxima_pagina = response.css('div.ui a::attr(href)')[-1].extract()
            if proxima_pagina is not None:
                yield response.follow(proxima_pagina, callback = self.parse)
        
    def parse_conteudo(self, response):
        
        link = response.url
        titulo = response.css('h1::text').extract_first()
        autor = response.css('.texto-autor::text').extract_first()
        dt_postagem = response.css('.exibe-texto span::text').extract_first()
        texto = "".join(response.css(".exibe-texto p::text")[3:].extract())
        site = 'mototour'
        
        #tratamento dos dados
        
        data_tratada = dt_postagem[:-6]
        
        texto = "".join(texto.replace('\r', ''))
        texto = "".join(texto.replace('\n', ''))
        texto = texto.replace('Notícias relacionadas','')
        texto = texto.replace('Agencia Infomoto','')
        texto = texto.replace('Agência Infomoto','')
        texto = texto.replace('Agência INFOMOTO','')
        texto = texto.replace('Infomoto','')
        texto = texto.lstrip(' ')
        texto = texto.rstrip(' ')
        
        items = MototourItem(titulo = titulo, autor = autor, dt_postagem = data_tratada, texto = texto, link = link, site = site)
 
        yield items

