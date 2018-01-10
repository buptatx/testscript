#! -*- coding:utf-8 -*-

import base64
import sys

from Crypto.Cipher import AES


class ASEncrypt():
    """
    基于ASE.ECB/PKCS5算法对输入字符串进行加解密
    """
    def __init__(self):
        self.key = "UymLGWztn9eWhLIR"
        self.clipher = AES.new(self.key, AES.MODE_ECB)

    def align_inStr(self, inStr):
        """
        对待加密字符串进行填充
        如果待加密字符串的长度不是ASE.block_size的整数倍，则填充至整数倍
        :param inStr: 待加密的字符串
        :return:填充后的待加密字符串，长度为ASE.block_size的整数倍
        """
        delta = AES.block_size - len(inStr) % AES.block_size
        if delta != 0:
            inStr += chr(delta) * delta
        return inStr

    def encrypt_inStr(self, inStr):
        """
        基于ASE.ECB/PKCS5算法对输入字符串进行加密
        :param inStr: 待加密的原始字符串
        :return:基于ASE.ECB/PKCS5加密后的结果
        """
        return self.clipher.encrypt(self.align_inStr(inStr))

    def decrypt_enStr(self, inStr):
        """
        基于ASE.ECB/PKCS5算法对输入字符串进行解密密
        :param inStr: 基于ASE.ECB/PKCS5加密后的结果
        :return:待加密的原始字符串
        """
        inStr += (len(inStr) % 4) * "="

        decryptByts = base64.urlsafe_b64decode(inStr)
        msg = self.clipher.decrypt(decryptByts)

        #截取解析结果，去除填充部分
        paddingLen = ord(msg[len(msg) - 1])
        return msg[0:-paddingLen]

    def get_urlsafe_encrypt(self, inStr):
        encrypt_str = self.encrypt_inStr(inStr)
        return base64.urlsafe_b64encode(encrypt_str)


if __name__ == "__main__":
    mCrypter = ASEncrypt()

    if len(sys.argv) == 3:
        if sys.argv[1] == "e":
            print mCrypter.get_urlsafe_encrypt(sys.argv[2])
        elif sys.argv[1] == "d":
            print mCrypter.decrypt_enStr(sys.argv[2]).decode("utf-8")
        else:
            print "usage:\r\n python ASEcrypter.py [e|d] inputStr"
    else:
        print "usage:\r\n python ASEcrypter.py [e|d] inputStr"