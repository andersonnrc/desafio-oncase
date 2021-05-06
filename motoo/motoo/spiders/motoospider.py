import scrapy
from ..items import MotooItem

class MotooSpider(scrapy.Spider):
    
    name = "motoo-crawler"
    
    start_urls = ['https://www.motoo.com.br/noticias/?n=1']
    
    def parse(self, response):
        
        conteudo = response.css('div.row')
        
        for campos in conteudo:    
            link = campos.css('div.header_title a::attr(href)').extract_first()
            
            yield response.follow(link, self.parse_conteudo)
   
            proxima_pagina = response.css('ul.pagination a::attr(href)')[4].extract()
            if proxima_pagina is not None:
                yield response.follow(proxima_pagina, callback = self.parse)
        
    def parse_conteudo(self, response):
        
        link = response.url
        titulo = response.css('h1::text').extract_first()
        autor = response.css('span.author-page .author-link::text').extract_first()
        dt_postagem = response.css('div.author_and_date span::text').extract_first()
        texto = "".join(response.css("div.body ::text").extract())
        tags = response.css('div.meta-tags a::text').extract()
        site = 'motoo'
        
        #tratamento dos dados
        autor = "".join(autor.replace('\r', ''))
        autor = "".join(autor.replace('\n', ''))
        autor = autor.lstrip(' ')
        autor = autor.rstrip(' ')
        
        dt_postagem = "".join(dt_postagem.replace('\r', ''))
        dt_postagem = "".join(dt_postagem.replace('\n', ''))
        dt_postagem = dt_postagem.lstrip(' ')
        dt_postagem = dt_postagem.rstrip(' ')
        data_tratada = dt_postagem[:-6]
        
        texto = "".join(texto.replace('\r', ''))
        texto = "".join(texto.replace('\n', ''))
        texto = texto.replace('(adsbygoogle = window.adsbygoogle || []).push({});','')
        texto = texto.lstrip(' ')
        texto = texto.rstrip(' ')
            
        items = MotooItem(titulo = titulo, autor = autor, dt_postagem = data_tratada, tags = tags, texto = texto, link = link, site = site)
 
        yield items

