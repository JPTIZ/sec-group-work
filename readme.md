INE5429 - Trabalho em Grupo
===========================

Integrantes
-----------

- João Paulo Taylor Ienczak Zanette
- Larissa Taw Rumiana de Oliveira

Vídeo de apresentação
---------------------

<https://youtu.be/Ajbl9Y7p25A>

Instalação
----------

OBS: Presume-se que **Python 3 já esteja instalado**.

### Requisitos

- Python 3.7+
- pyOpenSSL 19+
- [carl](https://gitlab.com/tarcisioe/carl)

### Instalando em uma Venv com Poetry

Para instalar o pacote + dependências em uma Virtualenv, pode-se utilizar o
[Poetry](https://github.com/sdispater/poetry).

```console
$ python3 -m ensurepip       # Caso não tenha `pip`
$ pip install --user poetry  # Instalação do Poetry


$ git clone https://github.com/jptiz/sec-group-work
$ cd sec-group-work
$ poetry install
```

Desintalação
------------

Apenas exclua a pasta `sec-group-work`.

Uso
---

> OBS: Se você instalou com Poetry, recomendase executar, na pasta do
> repositório:
>
> ```console
> $ poetry shell
> ```

### Help

```console
$ python -m simpkcs12 --help
usage: simpkcs12.py [-h] {sign,verify} ...

positional arguments:
  {sign,verify}
    sign         Signs document, generating ".sig" suffix.
    verify       Checks if file signature is valid.

optional arguments:
  -h, --help     show this help message and exit
```


### Assinar um arquivo

```console
$ python -m simpkcs12 sign --help
usage: simpkcs12.py sign [-h] [--encoding ENCODING] [--digest DIGEST]
                         document certificate password

Signs document, generating ".sig" suffix.

positional arguments:
  document
  certificate
  password

optional arguments:
  -h, --help           show this help message and exit
  --encoding ENCODING
  --digest DIGEST
```

Exemplo:

```console
$ ls
mycert.p12 myfile.ext
$ python -m simpkcs12 sign myfile.ext mycert.p12 secretpass123
$ ls
mycert.p12 myfile.ext myfile.sig
```

### Verificar se um arquivo está assinado

```console
$ python -m simpkcs12 verify --help
usage: simpkcs12.py verify [-h] [--encoding ENCODING] [--digest DIGEST]
                           document signature certificate password

Checks if file signature is valid.

positional arguments:
  document
  signature
  certificate
  password

optional arguments:
  -h, --help           show this help message and exit
  --encoding ENCODING
  --digest DIGEST
```

Exemplo:

```console
$ python -m simpkcs12 verify myfile.ext myfile.sig mycert.p12 secretpass123
Valid signature
$ python -m simpkcs12 verify myfile.ext myfile.sig wrongcert.p12 secretpass123
Wrong signature
```
