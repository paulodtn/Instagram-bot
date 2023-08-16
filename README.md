# Projeto-de-istagram-bot
Criando um mecanismo de automação para comentar e marcar em posts

# Comentando e Marcando em Post

Este é um projeto que visa criar um mecanismo de automação para comentar e marcar em post de redes sociais usando Python 3, VS Code, Selenium, time, secrets e random.

## Tecnologias

Este projeto usa as seguintes tecnologias:

- Python 3: uma linguagem de programação de alto nível, interpretada, de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte.
- VS Code: um editor de código-fonte desenvolvido pela Microsoft para Windows, Linux e macOS, que inclui suporte para depuração, controle de versionamento Git, realce de sintaxe, complementação inteligente de código, snippets e refatoração de código.
- Selenium: um conjunto de ferramentas que automatiza navegadores web. Ele é usado principalmente para testar aplicações web, mas também pode ser usado para outros fins, como scraping ou automação de tarefas repetitivas.
- time: um módulo Python que fornece várias funções relacionadas ao tempo, como obter o tempo atual, formatar e analisar datas e horas, medir intervalos de tempo e implementar pausas.
- secrets: um módulo Python que gera números aleatórios seguros para gerenciar dados confidenciais, como senhas, tokens ou chaves secretas.
- random: um módulo Python que implementa geradores pseudoaleatórios para vários tipos de dados, como números inteiros, reais, binários ou sequências.

## Como funciona

O projeto consiste em um script Python que usa o Selenium para acessar uma rede social, fazer login com uma conta previamente cadastrada, buscar por posts relacionados a um tema específico e comentar neles com uma mensagem aleatória e uma marcação de outro usuário. O script usa os módulos time, secrets e random para gerar tempos de espera, senhas e mensagens aleatórias.

## Como usar

Para usar este projeto, você precisa ter instalado o Python 3, o VS Code e o Selenium na sua máquina. Você também precisa ter uma conta na rede social que deseja usar e um arquivo chamado `config.py` que contém as seguintes variáveis:

- `username`: o nome de usuário da sua conta na rede social
- `password`: a senha da sua conta na rede social
- `theme`: o tema que você quer buscar nos posts (por exemplo, "música", "esporte", "política", etc.)
- `messages`: uma lista de strings com as possíveis mensagens que você quer comentar nos posts (por exemplo, ["Adorei!", "Muito bom!", "Show!", etc.])
- `users`: uma lista de strings com os nomes de usuários que você quer marcar nos comentários (por exemplo, ["@joao", "@maria", "@pedro", etc.])

Depois de ter tudo configurado, basta executar o script `main.py` no VS Code e esperar que ele faça o trabalho por você. Você pode ver o resultado na sua conta da rede social.

## Aviso

Este projeto é apenas para fins educacionais e de demonstração. Não me responsabilizo pelo uso indevido ou abusivo deste projeto. Respeite as regras e políticas da rede social que você usar e não incomode ou ofenda outros usuários com os seus comentários. Use este projeto com moderação e bom senso.
