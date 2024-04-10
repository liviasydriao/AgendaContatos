from main import*

agenda = Agenda()
contato1 = ContatoProfissional('Livia','85999773136','empresa A','Analista')
contato2 = ContatoPessoal('Saulo','85999773026','26/05/1992')
contato3 = ContatoProfissional('Mel','85999773027','empresa B','Gerente')
contato4 = ContatoProfissional('Leticia','85999773028','empresa C','Servidor')

agenda.adicionar_contato(contato1)
agenda.adicionar_contato(contato2)
agenda.adicionar_contato(contato3)
agenda.adicionar_contato(contato4)

agenda.exibir_info()