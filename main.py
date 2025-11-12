import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df_friends = pd.read_csv("data/friends.csv")


df_h1 = df_friends.groupby("duration_in_minutes").median("total_votes")

# Gráfico
plt.figure(figsize=(4,4))
sns.barplot(data=df_h1, x=df_h1.index, y="total_votes", color="#CC241B", label=df_h1["total_votes"])
plt.xlabel("Duración de episodio (minutos)")
plt.ylabel("Mediana de votos totales por duración")
plt.title("Mediana de votos totales por duración de episodio")
plt.savefig("img/grafico_h1.png")
plt.close()


df_h2 = df_friends[["season", "episode", "rating"]]
primero = df_h2.groupby("season").head(1)
ultimo = df_h2.groupby("season").tail(1)
df_h2 = pd.concat([primero, ultimo]).sort_values(["season", "episode"])

# Gráfico
sns.barplot(data=df_h2, x="season", y="rating", hue="episode", palette="dark:#F8DB01")
plt.xlabel("Temporada")
plt.ylabel("Rating")
plt.title("Rating por primer y último episodio de temporada")
plt.legend(bbox_to_anchor=[1,0], loc="lower right")
plt.savefig("img/grafico_h2.png")
plt.close()

df_h3 = (df_friends.groupby("season")["rating"].sum().reset_index().rename(columns={"rating":"rating_total"}))

# Gráfico
sns.lineplot(data=df_h3, x="season", y="rating_total", marker="o", color="#465B95")
plt.title("Rating total por temporada")
plt.xticks(df_h3["season"])
plt.xlabel("Temporada")
plt.ylabel("Rating total")
plt.axis("tight")
plt.savefig("img/grafico_h3.png")
plt.close()

df_h4 = pd.merge(df_friends.groupby("director")["total_votes"].mean().reset_index(), 
                 df_friends.groupby("director")["episode"].count().reset_index()).sort_values("total_votes", ascending=False)

# Gráfico
fig, ax = plt.subplots()
plt.barh(df_h4["director"], df_h4["total_votes"], color="#CC241B")
plt.title("Director con episodios más votados")
ax.set_xlabel("Votos totales")
ax.set_ylabel("Director")
ax.invert_yaxis()
plt.savefig("img/grafico_h4.png")
plt.close()

df_h5 = (df_friends.groupby("special_episode")["rating"].mean().reset_index())

# Gráfico
plt.pie(df_h5["rating"], autopct="%1.2f%%", colors=["#2E4170", "#F8DB01"])
plt.title("Rating de episodios especiales (S/N)")
plt.legend("NS", loc="upper left")
plt.savefig("img/grafico_h5.png")
plt.close()