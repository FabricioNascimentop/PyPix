from efipay import EfiPay

credentials = {
    'client_id': 'Client_Id_49d4e517fe1e8aca725c1359c653d9df07293ba9',
    'client_secret': 'Client_Secret_757e76f9f34f1f7f2f3e42ff535bf55c701ab87d',
    'sandbox': True,
    'certificate': 'C:\TheBigPython\PyProjects\PyPix\homologacao-535316-teste homologação_cert.pem'
}

gn = EfiPay(credentials)

body = {
    'calendario': {
        'expiracao': 3600
    },
    'devedor': {
        'cpf': '02217733206',
        'nome': 'Francisco da Silva'
    },
    'valor': {
        'original': '123.45'
    },
    'chave': '71cdf9ba-c695-4e3c-b010-abb521a3f1be',
    'solicitacaoPagador': 'Cobrança dos serviços prestados.'
}

headers = {
    'x-skip-mtls-checking': 'false'
}

params = {
    'chave': 'fabricio_nascimento2014@hotmail.com'
}

body = {
    'webhookUrl': 'https://pix.gerencianet.com.br/webhooks/chain-pix-sandbox.crt'
}

response =  gn.pix_config_webhook(params=params, body=body, headers=headers)
print(response)
