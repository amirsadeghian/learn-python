score = input("Enter Score: ")
if score >= 0.9:
    out= 'A'
elif score >= 0.8:
    out= 'B'
elif score >= 0.7:
    out= 'C'
elif score >= 0.6:
    out = 'D'
elif score < 0.6:
    out = 'F'
else:
    out = 'Error!'
print(out)
quit()