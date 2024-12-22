import pyinstaller_versionfile

pyinstaller_versionfile.create_versionfile(
    output_file="versionfile.txt",
    version="1.0.0v",
    company_name="My Imaginary Company",
    file_description="Dandilion",
    internal_name="Dandilion",
    legal_copyright="Dandilion © 2024",
    original_filename="Dandilion.exe",
    product_name="Dandilion",
    translations=[0, 1200]
)