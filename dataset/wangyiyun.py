# python3.6                                
# encoding    : utf-8 -*-                            
# @author     : YingqiuXiong
# @e-mail     : 1916728303@qq.com                                    
# @file       : wangyiyun.py
# @Time       : 2021/10/12 21:06

from Crypto.Cipher import AES
import base64
import requests
import json

headers = {
    # 'Cookie': 'appver=1.5.0.75771;',
    'Referer': 'http://music.163.com/',
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
}

first_param = "{rid:\"30953009\", offset:\"0\", total:\"true\", limit:\"20\", csrf_token:\"\"}"
# second_param = "010001"
# third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
forth_param = "0CoJUm6Qyw8W8jud"


def get_params():
    iv = b"0102030405060708"
    first_key = forth_param
    second_key = 16 * 'F'
    h_encText = AES_encrypt(first_param.encode(), first_key, iv)  # 第一个参数要更改
    print(h_encText)
    h_encText = AES_encrypt(h_encText, second_key, iv)
    print(h_encText)
    return h_encText


def get_encSecKey():
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey


def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    text2 = bytes(pad * chr(pad), encoding='gbk')  # 这里也要改
    text3 = text + text2  # 这里也要改
    encryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text3)
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text


def AES_decrypt(text, key, iv):
    decrypt_text = base64.b64decode(text)
    decryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    decrypt_text = decryptor.decrypt(decrypt_text)
    return decrypt_text


def get_json(url, params, encSecKey):
    data = {
        "params": params,
        "encSecKey": encSecKey
    }
    response = requests.post(url, headers=headers, data=data)
    return response.content


if __name__ == "__main__":
    # url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_30953009/?csrf_token="
    url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
    # url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
    params = get_params()
    encSecKey = get_encSecKey()
    json_text = get_json(url, params, encSecKey)
    json_dict = json.loads(json_text)
    print(json_dict)
    print(json_dict['total'])
    for item in json_dict['comments']:
        print(item['content'])
        # print(item['content'].encode('utf8', 'ignore'))
        # print(item['content'].encode('gbk', 'ignore'))

    # iv = b"0102030405060708"
    # first_key = forth_param
    # second_key = 16 * 'F'
    # # text = first_param
    # # # 两步加密
    # # text = text.encode()
    # # encrypt_text_1 = AES_encrypt(text=text, key=first_key, iv=iv)
    # # print(encrypt_text_1)
    # # encrypt_text_2 = AES_encrypt(text=encrypt_text_1, key=second_key, iv=iv)
    # # print(encrypt_text_2)
    # encrypt_text_2 = "wfwz5FzshlkjR0Vhzt+75R8rmMvBjdy8zj2XmK19cK/BOs55rvlMqag+gcEHGmi6zefF/3J2TQVmU3fTvmOPyVUBHHAr5AG1S0VEsloNo1OUzoxTutG1fd9dI+uHtMf2lIueGPMz9HZpj7gNHGeHbrXiMs46Rr91zxJSw9JX0kXsG9VSnjqkx5cF8bCrE76p1LadCtBPmh1OQoGYmveDlEWXTLEd4B+XQreLw4QeU0wQA3UDdgJYrA26mxrVSOSCzENT22VzQhtSbH86rG3GVQ=="
    # # 两步解密
    # decrypt_text_2 = AES_decrypt(text=encrypt_text_2, key=second_key, iv=iv)
    # print(decrypt_text_2)
    # decrypt_text_1 = AES_decrypt(text=decrypt_text_2, key=first_key, iv=iv)
    # print(decrypt_text_1)
    # print(decrypt_text_1.decode())




    # from Crypto.Cipher import AES
    # from binascii import b2a_hex, a2b_hex
    #
    # message = "我爱中国"
    # key = 'aes_keysaes_keysaes_keys'
    # mode = AES.MODE_OFB
    # cryptor = AES.new(key.encode('utf-8'), mode, b'0000000000000000')
    # length = 16
    # count = len(message)
    # if count % length != 0:
    #     add = length - (count % length)
    # else:
    #     add = 0
    # message = message + ('\0' * add)  # 上面 mode 为 MODE_OFB 时，信息长度要处理成16的倍数
    # ciphertext = cryptor.encrypt(message.encode('utf-8'))
    # result = b2a_hex(ciphertext)
    # print(result.decode('utf-8'))
    #
    # cryptor = AES.new(key.encode('utf-8'), mode, b'0000000000000000')
    # plain_text = cryptor.decrypt(a2b_hex(result))
    # print(plain_text.decode('utf-8').rstrip('\0'))
