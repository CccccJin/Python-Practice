str = 'X-DSPAM-Confidence: 0.8475'

maohao = str.find(':')
extract = str[maohao+2:]

print(float(extract))


