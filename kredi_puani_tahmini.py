#Gerekli kütüphanelerin yüklenmesi
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

#veri okuma işlemi
veri = pd.read_csv("veri.csv")
print(veri) #Verinin hepsi
print(veri.head()) #ilk 5 satır
print(veri.info())  #veri hakkında bilgi
#print(veri.isnull().sum()) #veride boş değer yok

#-----------------------------------GRAFİK OLUŞTURMA VE GÖSTERME-----------------------------------------

# Kredi puanı dağılımını sayma
counts = veri.groupby(['Occupation', 'Credit_Score']).size().reset_index(name='Count')
# Sütun grafiği oluşturma
fig1 = px.bar(counts, 
x='Occupation', 
y='Count', 
color='Credit_Score', 
title='Kredi Puanının Mesleklere Göre Dağılımı',
color_discrete_map={'Poor':'#de1010', 
                    'Standard':'#ff71fb', 
                    'Good':'#5c8cf9'})

fig1.show()

#-----------------------------------------------------------------------------------------------------------
fig = sp.make_subplots(rows=1, cols=2, subplot_titles=('Kredi Puanının Aylık Maaşa Göre Dağılımı',
                                                        'Kredi Puanının Yıllık Gelire Göre Dağılımı'))
#Kutu Grafiği
fig2 = px.box(veri, 
x="Credit_Score", 
y="Monthly_Inhand_Salary",
color = "Credit_Score",
title="Kredi Puanının Aylık Maaşa Göre Dağılımı",
color_discrete_map={'Poor':'#de1010', 
                    'Standard':'#ff71fb', 
                    'Good':'#5c8cf9'})
for trace in fig2.data:
    fig.add_trace(trace, row=1, col=1)

#Kutu Grafiği
fig3 = px.box(veri,
x ='Credit_Score',
y ='Annual_Income',
title='Kredi Puanının Yıllık Gelire Göre Dağılımı',
color = 'Credit_Score',
color_discrete_map={'Poor':'#de1010', 
                    'Standard':'#ff71fb', 
                    'Good':'#5c8cf9'})
for trace in fig3.data:
    fig.add_trace(trace, row=1, col=2)

# Grafiği gösterme
fig.update_layout(title_text="Kredi Puanı Kutu Grafikleri", showlegend=False)
fig.show()

#-------------------------------------------------------------------------------------------------------------
fig_bank = sp.make_subplots(rows=1, cols=2,subplot_titles =('Kredi Puanının Banka Hesap Sayısına Göre Dağılımı',
                                                            'Kredi Puanının Kredi Karta Sahip Olma Sayısına Göre Dağılımı'))
#Ortalama hesap sayıları alma
ort_bank_account = veri.groupby('Credit_Score')['Num_Bank_Accounts'].mean().reset_index()
#Sütün Grafiği
fig4 = px.bar(ort_bank_account, 
x='Credit_Score',
y='Num_Bank_Accounts', 
title='Kredi Puanının Banka Hesap Sayısına Göre Dağılımı',
color='Credit_Score',
color_discrete_map={'Poor':'#de1010', 
                    'Standard':'#ff71fb', 
                    'Good':'#5c8cf9'})
for trace in fig4.data:
    fig_bank.add_trace(trace,row=1,col=1)

#Ortalama kredi kart sayıları alma
ort_credit_cart = veri.groupby('Credit_Score')['Num_Credit_Card'].mean().reset_index()
#Sütün Grafiği
fig5= px.bar(ort_credit_cart, 
x='Credit_Score',
y='Num_Credit_Card', 
title='Kredi Puanının Kredi Karta Sahip Olma Sayısına Göre Dağılımı',
color='Credit_Score',
color_discrete_map={'Poor':'#de1010', 
                    'Standard':'#ff71fb', 
                    'Good':'#5c8cf9'})
for trace in fig5.data:
    fig_bank.add_trace(trace,row=1,col=2)

fig_bank.show()
