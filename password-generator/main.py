import random
import string
import datetime


PASSWORD_NUMBER = int(input("Combien de mot de passe voulez-vous générer ? "))
CHAR_COUNT = int(input("Combien de caractères au total ? "))
NUMBER_COUNT = int(input("Combien de nombres ? "))
SPECIAL_CHAR_COUNT = int(input("Combien de caractères spéciaux ? "))


def random_char(length: int):
    return random.sample(string.ascii_letters, length)


def random_special_char(length: int):
    special_char = []
    for i in range(length):
        special_char.append(random.choice('!$%&()*+,_`{|$%&-.:;<=>?@!$%&([]^_`$%{|}~'))

    return special_char


def random_num(length: int):
    digits = []
    for i in range(length):
        digits.append(str(random.randint(0, 9)))

    return digits


# Fonction pour exporter les mots de passes dans un fichier externe sur notre ordinateur
def export_generated_pwd(passwords: dict):
    date = datetime.datetime.now().strftime("%Y-%m-%dT%H%M%S")
    # Nom du fichier
    file_name = "{}_generated_passwords".format(date)

    # Extension du fichier
    file_extension = ".txt"

    # Demande où l'utilisateur veut que son fichier soit sauvegardé
    file_path = input("Dans quel dossier souhaitez-vous sauvegardé les mots de passe ?")
    complete_file_path = f"{file_path}/{file_name}{file_extension}"

    #Création du fichier où sera stocké les mots de passe
    with open(complete_file_path, 'w') as file:
        # Écrire dans le fichier les mots de passes générés
        for index, password in passwords.items():
            file.write(f"{index} : {password}\n")

    file.close()
    print("Le fichier a été exporté avec succès dans le dossier suivant : {}".format(complete_file_path))


# Fonction principale qui appelle toutes les autres fonctions
def main():
    # Déclaration du dictionnaire qui contiendra tous les mots de passes générés
    generated_passwords = dict()

    # Générer le nombre de mot de passe en fonction de l'entrée PASSWORD_NUMBER
    for i in range(0, PASSWORD_NUMBER):
        password_values = random_char(int(CHAR_COUNT - NUMBER_COUNT - SPECIAL_CHAR_COUNT)) + \
                          random_num(int(NUMBER_COUNT)) + \
                          random_special_char(int(SPECIAL_CHAR_COUNT))
        # Melanger aléatoirement tous les éléments de la liste
        random.shuffle(password_values)

        # Concatener / fusionner tous les éléments de la liste
        generated_password = ''.join(password_values)

        # Clé du dictionnaire (Exemple: mot de passe #1)
        generated_password_index = str("Mot de passe #{}".format(i + 1))
        generated_passwords[generated_password_index] = generated_password

    export_generated_pwd(generated_passwords)


if __name__ == "__main__":
    main()
