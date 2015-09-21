emails = re.findall('(?:\\n.*,\s.*?,.*,)(.*)(?:\\n)', faculty)
with open('emails.csv', 'w') as f:
    writer = csv.writer(f, delimiter=' ')
    for email in emails:
        writer.writerow([email])