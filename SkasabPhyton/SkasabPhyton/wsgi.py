"""
Configuração WSGI para o projeto sqldjango.

Este módulo contém o aplicativo WSGI usado pelo servidor de desenvolvimento do Django
e quaisquer implementações de produção WSGI. Deve expor uma variável de nível de módulo
chamado `` application``. Os comandos `` runserver`` e `` runfcgi` do Django descobrem
esta aplicação através da configuração `` WSGI_APPLICATION``.

Normalmente você terá o aplicativo Django WSGI padrão aqui, mas também
pode fazer sentido substituir todo o aplicativo Django WSGI por um personalizado
no Django. Por exemplo, você poderia introduzir o WSGI
middleware aqui, ou combinar um aplicativo Django com um aplicativo de outro
estrutura.
"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SkasabPhyton.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
