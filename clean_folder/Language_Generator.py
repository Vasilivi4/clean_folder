import os
from clean_folder.generator_file_ue import generate_empty_files_ue
from clean_folder.generator_file_uk import generate_empty_files_uk

new_chr = input("Vvedite Y/N: ")


if new_chr == "Y":
    output_directory_ue = "C:\\users\\Num\\clean_folder\\sort_test\\name_ue"
    generate_empty_files_ue(output_directory_ue)

    output_directory_uk = "C:\\users\\Num\\clean_folder\\sort_test\\name_uk"
    generate_empty_files_uk(output_directory_uk)
else:
    print("Program_completed")
