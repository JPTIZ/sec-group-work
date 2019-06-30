from dataclass import dataclasses
from sys import argv

from OpenSSL import crypto


def load_pkcs12(filename: Path, password: str) -> crypto.PKCS12:
    '''Loads file containing PKCS12 keys.'''
    with open(filename, 'rb') as f:
        return crypto.load_pkcs12(f.read(), password.encode('utf8'))


def sign(document: str, certificate):
    '''Signs file with given certificate.'''
    # TODO
    pass


def verify(document: Path, certificate):
    '''Checks if file signature is valid.'''
    # TODO
    pass


if __name__ == '__main__':
    p12 = load_pkcs12(argv[1], argv[2])

    print(p12.get_certificate())
    print(p12.get_privatekey())
    print(p12.get_ca_certificates())
