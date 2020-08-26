from cli_badges import badge

successBadge = badge('success','8', messagebg='green',messagecolor='black')
failedBadge = badge("failed",'1',messagebg='red')
skippedBadge = badge('skipped', '1', messagebg='yellow',messagecolor='black')

print(successBadge, failedBadge, skippedBadge, "")