# Strings

str = "X-DSPAM-Confidence: 0.8475"
srt = str.find(':')
port = str[srt+2:]
value = float(port)
print(value)
