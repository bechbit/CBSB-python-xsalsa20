import os
import shutil
import rclone

def encrypt_file(source_file, destination_file, password):
    """Encrypts the contents of the source file to the destination file using the xsalsa20 cipher and poly1305 verification.

    Args:
        source_file (str): The path to the source file.
        destination_file (str): The path to the destination file.
        password (str): The password to use for encryption.
    """

    client = rclone.Rclone()
    client.config.update(
        remote="encrypted",
        encryption_mode="xsalsa20+poly1305",
        password=password,
    )

    client.copy(source_file, destination_file)

def encrypt_hard_drive(hard_drive_path, backup_directory, password):
    """Encrypts the contents of the hard drive at `hard_drive_path` to the directory `backup_directory` using the xsalsa20 cipher and poly1305 verification.

    Args:
        hard_drive_path (str): The path to the hard drive.
        backup_directory (str): The path to the directory to store the backup.
        password (str): The password to use for encryption.
    """

    # Encrypt all the files in the hard drive.
    for root, dirs, files in os.walk(hard_drive_path):
        for file in files:
            source_file = os.path.join(root, file)
            destination_file = os.path.join(backup_directory, file)
            encrypt_file(source_file, destination_file, password)

# Get the path to the hard drive you want to encrypt.
hard_drive_path = "C:\\"

# Create a new directory to store the backup.
backup_directory = "C:\\Backups"

# Create a new password for the encryption.
password = input("Enter a password for the encryption: ")

# Encrypt the hard drive.
encrypt_hard_drive(hard_drive_path, backup_directory, password)

# Print a success message.
print("The hard drive has been encrypted and backed up successfully!")
