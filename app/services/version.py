import pyinstaller_versionfile

pyinstaller_versionfile.create_versionfile(
    output_file="versionfile.txt",
    version="1.2.3.4",
    company_name="My Imaginary Company",
    file_description="Dandilion",
    internal_name="Dandilion",
    legal_copyright="Dandilion © 2024",
    original_filename="Dandilion.exe",
    product_name="Dandilion",
    translations=[0, 1200]
)