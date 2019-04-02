from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABcob7STDFn-6OrtaekrFhUWs_FJOlLyCds029GByjvHsyJQGcQs5iMYQnNKwgo563eUcaa6qTpyHSE-51Lzk6RKRS99dWh2L1aEUrLVaCzd7qTa-dj750y7fwxtSoxA32S2lbjUhN7cfjxskgoGSbMHLYlHH6bextc90tkx7ayhRb80VKiKRxCbBzSt112AJMS56hJ'

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == '__main__':
    main()
