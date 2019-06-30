# System libraries
from sys import argv
from pathlib import Path

# External libraries
from carl import command, REQUIRED
from OpenSSL import crypto


class Defaults:
    ENCODING = 'utf8'
    DIGEST = 'sha256'


@command
def main(subcommand = REQUIRED):
    pass


def load_pkcs12(
        filename: Path,
        password: str,
        encoding=Defaults.ENCODING
) -> crypto.PKCS12:
    '''Loads file containing PKCS12 keys.

    encoding (str): Password encoding.'''
    with open(filename, 'rb') as f:
        return crypto.load_pkcs12(f.read(), password.encode(encoding))


@main.subcommand
def sign(
        document: Path,
        certificate: Path,
        password: str,
        encoding=Defaults.ENCODING,
        digest=Defaults.DIGEST,
):
    '''Signs document, generating ".sig" suffix.'''
    p12 = load_pkcs12(certificate, password)

    with open(document, 'r') as f:
        contents = f.read().encode(encoding)

        sig = crypto.sign(p12.get_privatekey(), contents, digest)

    with open(f'{document.stem}.sig', 'wb') as f:
        f.write(sig)


@main.subcommand
def verify(
        document: Path,
        signature: Path,
        certificate: Path,
        password: str,
        encoding=Defaults.ENCODING,
        digest=Defaults.DIGEST,
):
    '''Checks if file signature is valid.'''
    p12 = load_pkcs12(certificate, password)

    with open(signature, 'rb') as f:
        sig = f.read()

    with open(document) as f:
        data = f.read().encode(encoding)

    try:
        crypto.verify(p12.get_certificate(), sig, data, digest)
    except:
        print('Wrong signature.')
        raise

    print('Valid signature')


if __name__ == '__main__':
    main.run()
