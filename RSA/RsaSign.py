from base64 import b64encode, b64decode
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

class RsaSign:
    """RSA签名验签"""
    def __init__(self):
        pass

    def private_key_signature(self,message, privatefile):
        # use private key certificate to signature
        privatekey = RSA.importKey(self._read_file(privatefile))
        signer = PKCS1_v1_5.new(privatekey)
        return b64encode(signer.sign(SHA.new(message.encode('utf-8'))))

    def public_key_verify(self,message, sign, publicfile):
        # use public key certificate to verify
        publickey = RSA.importKey(self._read_file(publicfile))
        verifier = PKCS1_v1_5.new(publickey)
        return verifier.verify(SHA.new(message.encode('utf-8')), b64decode(sign))

    def _read_file(self,file_path):
        with open(file_path, 'rb') as fp:
            return fp.read()


if __name__=='__main__':
    rsaSign=RsaSign()
    sign=rsaSign.private_key_signature('123456','private.pem')
    print(sign)

    res=rsaSign.public_key_verify('123456',sign,'public.pem')
    print(res)