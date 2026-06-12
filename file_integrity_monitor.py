import hashlib
import json
import os

# File to store original hashes
HASH_DB = "hash_database.json"


def calculate_hash(filepath):
    """
    Calculate SHA-256 hash of a file.
    """
    sha256 = hashlib.sha256()

    try:
        with open(filepath, "rb") as file:
            while chunk := file.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    except FileNotFoundError:
        return None


def create_baseline(files):
    """
    Create and store baseline hashes.
    """
    hashes = {}

    for file in files:
        file_hash = calculate_hash(file)

        if file_hash:
            hashes[file] = file_hash
            print(f"[+] Baseline created for: {file}")
        else:
            print(f"[-] File not found: {file}")

    with open(HASH_DB, "w") as db:
        json.dump(hashes, db, indent=4)

    print("\nBaseline hash database saved.")


def monitor_files():
    """
    Compare current hashes with stored hashes.
    """
    if not os.path.exists(HASH_DB):
        print("No baseline found. Create baseline first.")
        return

    with open(HASH_DB, "r") as db:
        stored_hashes = json.load(db)

    print("\nChecking file integrity...\n")

    for file, old_hash in stored_hashes.items():
        current_hash = calculate_hash(file)

        if current_hash is None:
            print(f"[!] File deleted: {file}")

        elif current_hash != old_hash:
            print(f"[WARNING] File modified: {file}")

        else:
            print(f"[OK] No changes: {file}")


def main():
    while True:
        print("\n=== File Integrity Monitoring Tool ===")
        print("1. Create Baseline")
        print("2. Monitor Files")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            files = input(
                "Enter file paths separated by commas: "
            ).split(",")

            files = [f.strip() for f in files]
            create_baseline(files)

        elif choice == "2":
            monitor_files()

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()