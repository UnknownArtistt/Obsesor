import pyfiglet
import hashlib
import itertools
import string
from tqdm import tqdm

def generate_hash(plaintext, algorithm):
    hash_func = hashlib.new(algorithm)
    hash_func.update(plaintext.encode('utf-8'))
    return hash_func.hexdigest()

def brute_force_crack(hash_value, algorithm, max_length):
    print("\nStarting Brute Force Attack, this will take time, relax and let Obsesor do the work...")
    print("---------------------------------------------------------------------------------------\n")
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    total_combinations = sum(len(characters) ** length for length in range(1, max_length + 1))

    for length in range(1, max_length + 1):
        for attempt in tqdm(itertools.product(characters, repeat=length), total=len(characters)**length, desc=f'Length {length}'):
            attempt = ''.join(attempt)
            if generate_hash(attempt, algorithm) == hash_value:
                return attempt
    return None

def dictionary_crack(hash_value, algorithm, dictionary_file, encoding='latin-1'):
    print("\nStarting Dictionary Attack, relax and let Obsesor do the work...")
    print("-------------------------------------------------------------\n")
    try:
        with open(dictionary_file, 'r', encoding=encoding) as file:
            words = file.readlines()
            for word in tqdm(words, desc='Dictionary attack'):
                word = word.strip()
                if generate_hash(word, algorithm) == hash_value:
                    return word
    except FileNotFoundError:
        print(f"Dictionary file '{dictionary_file}' not found.")
    return None

def showBanner():
    intro = pyfiglet.figlet_format("Obsesor", font="slant")
    print("\n----------------------------------------")
    print(intro + "      [+] Coded By AbyssWatcher [+]")
    print("----------------------------------------")

def showHelp():
    print("\nObsesor Usage =>")
    print("\n-help\t\tShows this help message visualizing the commands")
    print("-hash\t\tHashes the given text")
    print("-bruteforce\tTries to crack a hash using a brute force attack")
    print("-dictionary\tTries to crack a hash using a dictionary attack")
    print("-exit\t\tExits the program")
    print("--------------------------------------------------------")

def main():
    showBanner()
    showHelp()

    while(True):
        command = input("\nObsesor:~$ ")

        if command == "-help":
            showHelp()

        elif command == "-exit":
            print("\nFarewell my old friend, the abyss awaits...\n")
            break

        elif command == "-hash":
            plaintext = input("Enter the text to hash: ")
            algorithm = input("Enter the hash algorithm (e.g., md5, sha1, sha256): ").lower()
            hashed_text = generate_hash(plaintext, algorithm)
            print("Your hash => " + hashed_text)

        elif command == "-bruteforce":
            algorithm = input("Enter the hash algorithm (e.g., md5, sha1, sha256): ").lower()
            hash_to_crack = input("Enter the hash to crack: ")
            cracked = None

            max_length = int(input("Enter the maximum length for brute force attack: "))
            cracked = brute_force_crack(hash_to_crack, algorithm, max_length)

            if cracked:
                print(f"\nHash cracked :D -> The plaintext is: {cracked}")
            else:
                print("\nFailed to crack the hash :(")

        elif command == "-dictionary":
            algorithm = input("Enter the hash algorithm (e.g., md5, sha1, sha256): ").lower()
            hash_to_crack = input("Enter the hash to crack: ")
            dictionary_file = input("Enter the dictionary file path: ")
            encoding = input("Enter the dictionary file encoding (default is 'latin-1', press enter to use it): ") or 'latin-1'
            cracked = dictionary_crack(hash_to_crack, algorithm, dictionary_file, encoding)

            if cracked:
                print(f"\nHash cracked :D -> The plaintext is: {cracked}")
            else:
                print("\nFailed to crack the hash :(")

        else:
            print("\nInvalid Command, take a look to the Obsesor Usage and try again...")

if __name__ == "__main__":
    main()
