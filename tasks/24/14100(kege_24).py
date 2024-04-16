# 14100
f=open('txt/24-14100_14100.txt').readline()
m_s=[0]*len(f)
for i in range(len(f)-1):
    if  f[i:i+3] == 'ABC' or f[i:i+3] == 'BCB':
        m_s[i] = max(m_s[i],m_s[i-3]+3)
    if f[i]=='A' and ( f[i+1]=='B' or f[i+1]=='C')  or f[i]=='B' and ( f[i+1]=='A' or f[i+1]=='C') or f[i] =='C' and  (f[i+1]=='B' or f[i+1]=='A'):
        m_s[i] = max(m_s[i],m_s[i-2]+2)
print(max(m_s))
