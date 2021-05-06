import scrapy
from ..items import TudodemotosItem
from dateutil.parser import parse

class TudodemotosSpider(scrapy.Spider):
    
    name = "tudodemoto-crawler"
    numero_pagina = 3
    start_urls = ['https://tudodemotos.com.br/page/2/']
    
    def parse(self, response):
        
        items = TudodemotosItem()
        
        all_noticias = response.css('.td-block-row')
        
        for conteudo in all_noticias:    
            link = conteudo.css('.td-block-row a::attr(href)').extract_first()
            
            yield response.follow(link, self.parse_conteudo)
            
        proxima_pagina = 'https://tudodemotos.com.br/page/' + str(TudodemotosSpider.numero_pagina) + '/'
        if TudodemotosSpider.numero_pagina < 150:
            TudodemotosSpider.numero_pagina += 1
            
            yield response.follow(proxima_pagina, callback = self.parse)
            
            
    def parse_conteudo(self, response):
        
        link = response.url
        titulo = response.css('.entry-title::text').extract_first()
        autor = response.css('.td-post-author-name a::text').extract_first()
        dt_postagem = response.css('span.td-post-date time::attr(datetime)').extract_first()
        texto = "".join(response.css("div.td-post-content p::text").extract())
        tags = response.css('ul.td-tags li a::text').extract()
        site = 'tudodemotos'
        
        #tratamento dos dados
        data_tradada = parse(dt_postagem)
        data_tradada = str(data_tradada.day) + '/' + str(data_tradada.month) + '/' + str(data_tradada.year)
          
        items = TudodemotosItem(titulo = titulo, autor = autor, dt_postagem = data_tradada, tags = tags, texto = texto, link = link, site = site)
 
        yield items