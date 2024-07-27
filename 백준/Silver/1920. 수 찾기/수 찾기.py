n=input()
n_set=set(input().split())
m=input()
m_list=input().split()
m_set=set(m_list)
check_set=n_set & m_set
for i in m_list:
    if i in check_set:
        print(1)
    else:
        print(0)