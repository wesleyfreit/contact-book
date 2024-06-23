if __name__ == "__main__":
    while True:
        print("\n------------------")
        print("AGENDA DE CONTATOS")
        print("------------------")
        print("\nOpções da Agenda:\n")
        print("[1] - Salvar um contato")
        print("[2] - Ver todos os contatos")
        print("[3] - Ver todos os contatos favoritos")
        print("[4] - Atualizar dados de um contato")
        print("[5] - Marcar/Desmacar contato como favorito")
        print("[6] - Deletar um contato salvo")
        print("[7] - Sair do programa")

        try:
            option = int(input("\nInsira uma opção: "))

            match option:
                case 7:
                    print("\nO programa foi finalizado.")
                    break
                case _:
                    print("\nInsira uma opção válida!")
        except ValueError:
            print("\nInsira uma opção válida!")
        except Exception as error:
            print(error)
