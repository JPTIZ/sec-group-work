# System libraries
from sys import argv
from pathlib import Path

# External libraries
from carl import command, REQUIRED
from OpenSSL import crypto


@command
def main(subcommand = REQUIRED):
    pass


def load_pkcs12(filename: Path, password: str) -> crypto.PKCS12:
    '''Loads file containing PKCS12 keys.'''
    with open(filename, 'rb') as f:
        return crypto.load_pkcs12(f.read(), password.encode('utf8'))


@main.subcommand
def sign(document: Path, certificate: Path, password: str):
    '''Signs document, generating a file with "-signed" suffix.'''
    # TODO
    p12 = load_pkcs12(certificate, password)

    print(p12.get_certificate())
    print(p12.get_privatekey())
    print(p12.get_ca_certificates())


@main.subcommand
def verify(document: Path, certificate: Path, password: str):
    '''Checks if file signature is valid.'''
    pass


if __name__ == '__main__':
    main.run()
