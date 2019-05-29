from estimaciones.models import Estimacion
from requests import get,post
from bs4 import BeautifulSoup


class EstimacionBloomberg:

    url = 'https://www.bloomberg.com/quote'

    def estimar(self, fondo):
        pag = "{}/{}".format(self.url, fondo)
        result = get(url=pag)
        content = BeautifulSoup(result.content, "html.parser")
        links = content.findAll('a', attrs={'class': 'link__157cfc61'})

        return 123


class NotLoadedException(Exception):
    pass


class EstimacionFondo:
    estimador = EstimacionBloomberg()
    manager = Estimacion.objects

    def estimarFondo(self, fondo):
        if self.estimador is None:
            raise NotLoadedException
        valor = self.estimador.estimar(fondo)
        self.manager.create(valor=valor, fondo=fondo)
