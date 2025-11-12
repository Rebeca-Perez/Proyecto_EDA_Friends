"""
    Importar las librerías que se van a utilizar para el desarrollo,
"""
import pandas as pd
import matplotlib.pyplot as plt     
import seaborn as sns
import os

"""
    Comprobar si existe la carpeta img donde se guardarán los gráficos, si no está la crea.
"""
if not os.path.exists("./img"):
    os.mkdir("./img")
else:
    print("ya existe")   

"""
    Carga de datos en un Dataframe para evaluar que datos tenemos.
"""
df_friends = pd.read_csv("data/friends.csv")

"""
    Creación de Dataframe propio para hipótesis 1, 
    agrupación por duración de episodio y mediana de votos totales.
"""
df_h1 = df_friends.groupby("duration_in_minutes").median("total_votes")

"""
    Gráfico de barras de tamaño 4x4 para comprobar 
    número de votos por duración de episodio.
    Se definen ejes, color y tamaño de datos.
    Título y nombre de ejes.
    Se guarda en la carpeta img al ejecutarse.
    plt.close, no sobreescribe los gráficos.
"""
plt.figure(figsize=(4,4))
sns.barplot(data=df_h1, x=df_h1.index, y="total_votes", color="#CC241B", label=df_h1["total_votes"])
plt.xlabel("Duración de episodio (minutos)")
plt.ylabel("Mediana de votos totales por duración")
plt.title("Mediana de votos totales por duración de episodio")
plt.savefig("img/grafico_h1.png")
plt.close()

"""
    Creación de Dataframe propio para hipótesis 2. 
    Sacar primer y último episodio de cada temporada y ordenar por temporada.
"""
df_h2 = df_friends[["season", "episode", "rating"]]
primero = df_h2.groupby("season").head(1)
ultimo = df_h2.groupby("season").tail(1)
df_h2 = pd.concat([primero, ultimo]).sort_values(["season", "episode"])

"""
    Gráfico de barras para comprar si el rating es mayor en los últimos episodios.
    Se definen ejes, color y tamaño de datos.
    Título de gráfico, nombre de ejes.
    Se gaurda en la carpeta img al ejecutarse.
    plt.close no sobreescribe los gráficos.
"""
sns.barplot(data=df_h2, x="season", y="rating", hue="episode", palette="dark:#F8DB01")
plt.xlabel("Temporada")
plt.ylabel("Rating")
plt.title("Rating por primer y último episodio de temporada")
plt.legend(bbox_to_anchor=[1,0], loc="lower right")
plt.savefig("img/grafico_h2.png")
plt.close()

"""
    Creación de Dataframe para hipótesis 3. Se extrae la temporada y el rating.
    Se agrupa por la temporada, haciendo sumatorio del rating.
"""
df_h3 = (df_friends.groupby("season")["rating"].sum().reset_index().rename(columns={"rating":"rating_total"}))

"""
    Gráfico lineal de rating total por temporada,
    Se definen ejes, color y tamaño de datos.
    Título y nombre de los ejes.
    Cada vez que se ejecuta el script se guardan en la carpeta img con su nombre.
    plt.close(), para que no se sobreescriban los gráficos al guardarse.
"""
sns.lineplot(data=df_h3, x="season", y="rating_total", marker="o", color="#465B95")
plt.title("Rating total por temporada")
plt.xticks(df_h3["season"])
plt.xlabel("Temporada")
plt.ylabel("Rating total")
plt.axis("tight")
plt.savefig("img/grafico_h3.png")
plt.close()

"""
    Creación de Dataframe propio para la hipótesis 4, agrupación por director, 
    media de votos totales y conteo de episodios dirigidos.
"""
df_h4 = pd.merge(df_friends.groupby("director")["total_votes"].mean().reset_index(), 
                 df_friends.groupby("director")["episode"].count().reset_index()).sort_values("total_votes", ascending=False)

"""
    Gráfico de barras horizontales para mostrar el director con la media de episodios más votados en función de los dirigidos.
    Se definen ejes, color y tamaño de datos.
    Título de gráfico, nombre de ejes, se invierte el eje Y para que se entienda mejor el gráfico.
    Se guarda el gráfico en la carpeta img con su nombre al ejecutar el script.
    plt.close, para no sobreescribir los gráficos.
"""
fig, ax = plt.subplots()
plt.barh(df_h4["director"], df_h4["total_votes"], color="#CC241B")
plt.title("Director con episodios más votados")
ax.set_xlabel("Votos totales")
ax.set_ylabel("Director")
ax.invert_yaxis()
plt.savefig("img/grafico_h4.png")
plt.close()

"""
    Creación de Dataframe para hipótesis 5, agrupación por episodios especiales y media de rating.
"""
df_h5 = (df_friends.groupby("special_episode")["rating"].mean().reset_index())

"""
    Gráfico de quesos para visualizar si los episodios especiales tienen más rating.
    Se definen ejes, color y tamaño de datos.
    Título de gráfico, y posición de la etiqueta.
    Se guarda en la carpeta img al ejecutarse.
    plt.close para no se sobreescriben los gráficos.
"""
plt.pie(df_h5["rating"], autopct="%1.2f%%", colors=["#2E4170", "#F8DB01"])
plt.title("Rating de episodios especiales")
plt.legend(labels=["Ep.Normal", "Ep.Especial"], loc="upper left")
plt.savefig("img/grafico_h5.png")
plt.close()