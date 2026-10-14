from funcoes import (
    exercicio1_divisao,
    exercicio2_media,
    exercicio3_carga_horaria,
    exercicio4_saldo,
    exercicio5_aprovados,
)


def mostrar_menu():
    print("\nLISTA 1")
    print("1 - Exercício 1: Divisão")
    print("2 - Exercício 2: Média")
    print("3 - Exercício 3: Carga horária")
    print("4 - Exercício 4: Saldo bancário")
    print("5 - Exercício 5: Alunos aprovados")
    print("0 - Sair")


def main():
    while True:
        try:
            mostrar_menu()
            escolha = input("Escolha uma opção: ").strip()
        except EOFError:
            print("\nEntrada encerrada. Saindo...")
            break

        if escolha == "1":
            exercicio1_divisao()
        elif escolha == "2":
            exercicio2_media()
        elif escolha == "3":
            exercicio3_carga_horaria()
        elif escolha == "4":
            exercicio4_saldo()
        elif escolha == "5":
            exercicio5_aprovados()
        elif escolha == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

        try:
            input("\nPressione Enter para continuar...")
        except EOFError:
            print("\nEntrada encerrada. Saindo...")
            break


main()
