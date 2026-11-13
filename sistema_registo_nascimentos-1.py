class Mae:
    def __init__(self, nome, identificador):
        self.nome = nome
        self.identificador = identificador


class Medico:
    def __init__(self, nome):
        self.nome = nome


class Bebe:
    def __init__(self, numero, nome, genero, mae, medico):
        self.numero = numero
        self.nome = nome
        self.genero = genero
        self.mae = mae
        self.medico = medico


class SistemaNascimento:
    def __init__(self):
        self.bebes = []
        self.contador = 1

    def registar_nascimento(self):
        print("\n--- REGISTO DE NASCIMENTO ---")

        nome_mae = input("Nome da mãe: ")
        identificador = input("Identificador da mãe: ")

        nome_bebe = input("Nome do bebé: ")
        genero = input("Género (M/F): ").upper()

        while genero not in ["M", "F"]:
            print("Género inválido!")
            genero = input("Género (M/F): ").upper()

        nome_medico = input("Nome do médico: ")

        mae = Mae(nome_mae, identificador)
        medico = Medico(nome_medico)

        bebe = Bebe(
            self.contador,
            nome_bebe,
            genero,
            mae,
            medico
        )

        self.bebes.append(bebe)

        print("Número de identificação:", self.contador)
        print("Nascimento registado com sucesso!")

        self.contador += 1

    def consultar_bebe(self):
        identificador = input("Identificador da mãe: ")
        encontrado = False

        for bebe in self.bebes:
            if bebe.mae.identificador == identificador:
                print("\nNome do bebé:", bebe.nome)
                print("Género:", bebe.genero)
                print("Mãe:", bebe.mae.nome)
                print("Médico:", bebe.medico.nome)
                print("Número:", bebe.numero)
                encontrado = True

        if not encontrado:
            print("Nenhum registo encontrado.")

    def estatisticas(self):
        masculino = 0
        feminino = 0

        for bebe in self.bebes:
            if bebe.genero == "M":
                masculino += 1
            else:
                feminino += 1

        print("\n--- ESTATÍSTICAS ---")
        print("Total de nascimentos:", len(self.bebes))
        print("Masculinos:", masculino)
        print("Femininos:", feminino)

    def menu(self):
        while True:
            print("\n===== SISTEMA DE NASCIMENTOS =====")
            print("1 - Registar nascimento")
            print("2 - Consultar bebé")
            print("3 - Estatísticas")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.registar_nascimento()
            elif opcao == "2":
                self.consultar_bebe()
            elif opcao == "3":
                self.estatisticas()
            elif opcao == "0":
                print("Programa encerrado!")
                break
            else:
                print("Opção inválida!")


if __name__ == "__main__":
    sistema = SistemaNascimento()
    sistema.menu()
