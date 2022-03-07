from web3 import Web3

def sendTransaction(message):
    w3=Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/76f3c87aea71435a9b99d49ab3516237'))
    address='0x8419783bEBffd7fE15DbC4492e96B4464271FC07'
    privateKey='0xb42a1dda3def25634c39e0f0fcebe5fd8620a59006296de97e19f5fc76e55041'
    nonce=w3.eth.getTransactionCount(address)
    gasPrice=w3.eth.gasPrice
    value=w3.toWei(0,'ether')
    signedTx=w3.eth.account.signTransaction(dict(
        nonce=nonce,
        gasPrice=gasPrice,
        gas=100000,
        to='0x0000000000000000000000000000000000000000',
        value=value,
        data=message.encode('utf-8')
    ),privateKey)

    tx=w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId=w3.toHex(tx)
    return txId