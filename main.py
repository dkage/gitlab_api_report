import requests


# TODO Needs auth method

url = "https://10.68.13.200:8888/api/v4/projects/24/repository/commits?per_page=105"
print(url)

json_return = requests.get(url, verify=False)

html_output_file = open("commits.json", "w")
html_output_file.write(json_return.text)
html_output_file.close()
