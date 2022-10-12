# InstaBot :robot: :computer:
Projeto destinado a criação de automação para comentar e marcar em posts no Instagram.

## Instalação

Utilizar o arquivo `requirements.txt` para instalar o pacote necessário.

```bash
pip3 install -r requirements.txt
```

## Modo de uso
Para fazer uso da ferramenta, deve-se fornecer a conta cadastrada no Instagram e sua senha. 

| Parâmetro          | Descrição              |  Requisito |
| ------------------ | ---------------------- | ---------------- |
| --user             | Sua conta no Instagram |  obrigatório     |
| --password_account | Sua senha no instagram |  obrigatório     |
|                    |                        |                  |

## Limitações
-> Se a conta houver autenticação em dois fatores, a ferramenta não funcionará, pois identificará um acesso estranho.
