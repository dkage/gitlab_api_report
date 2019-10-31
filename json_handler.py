import json


# https://10.68.13.200:8888/api/v4/projects/24/repository/commits?per_page=900
with open('commits.json', 'r') as json_file:
    json_commits = json.load(json_file)


html_output = "<html><body>"
for element in reversed(json_commits):
    if "Merge branch" in element['message'] or "Merge remote" in element['message']:
        continue
    html_output += "<div>\n"
    html_output += "<h2>" + element["title"] + "</h2>\n"
    html_output += "<h3>Commit: " + element["short_id"] + "</h3>\n"
    message_line_breaks = element["message"].replace("\n", "<br />\n")
    html_output += "<p>" + element["message"] + "</p>"
    html_output += "<p></p>"
    html_output += "</div><br><br><br>\n"

html_output += "</body></html>"
print(html_output)


json_file.close()
html_output_file = open("output.html", "w")
html_output_file.write(html_output)
html_output_file.close()
