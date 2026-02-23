from functions.get_files_info import get_files_info

print("Results for current directory:")
results = get_files_info("calculator", ".")
indented_results = results.replace("\n", "\n  ")
print(f"  {indented_results}")

print("Results for 'pkg' directory:")
results = get_files_info("calculator", "pkg")
indented_results = results.replace("\n", "\n  ")
print(f"  {indented_results}")

print("Results for '/bin' directory:")
results = get_files_info("calculator", "/bin")
indented_results = results.replace("\n", "\n  ")
print(f"  {indented_results}")

print("Results for '../' directory:")
results = get_files_info("calculator", "../")
indented_results = results.replace("\n", "\n  ")
print(f"  {indented_results}")
