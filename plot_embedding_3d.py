import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
import psycopg2

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(projection='3d')
cmap = plt.get_cmap("tab20")

question = []
embeddings = []

try:
    conn = psycopg2.connect("host=localhost dbname=draks_bot_db user=draks_bot_user port=5444 password=UltraSuperSecretote")
    cur = conn.cursor()
    query = """ SELECT question, embedding FROM faqs """
    cur.execute(query)
    result = cur.fetchall()

    for row in result:
        question.append(row[0])
        vctr = np.array(row[1])
        embeddings.append(vctr)
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    cur.close()
    conn.close()

pca = PCA(n_components=3)
vis_dims = pca.fit_transform(embeddings)
#vis_dims.tolist()


"""
# Plot each sample category individually such that we can set label name.
for i, cat in enumerate(categories):
    sub_matrix = np.array(samples[samples["category"] == cat]["embed_vis"].to_list())
    x=sub_matrix[:, 0]
    y=sub_matrix[:, 1]
    z=sub_matrix[:, 2]
    colors = [cmap(i/len(categories))] * len(sub_matrix)
    ax.scatter(x, y, zs=z, zdir='z', c=colors, label=cat)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.legend(bbox_to_anchor=(1.1, 1))
"""