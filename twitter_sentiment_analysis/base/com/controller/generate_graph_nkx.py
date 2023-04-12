import networkx as nkx
import matplotlib.pyplot as plt
import community.community_louvain as cl
import os

def main_start_generate_graph(df,base_tag,login_secretkey):
    all_has_tags = list()
    for tweets in df:
        if tweets.get('hashtags'):
            for tags in tweets.get('hashtags'):
                all_has_tags.append((base_tag,tags))

    graph = nkx.Graph()
    graph.add_edges_from(all_has_tags)
    graph_photo = nkx.draw(graph)
    pos = nkx.spring_layout(graph)
    nkx.draw(graph, pos, node_size=1500, node_color='grey', font_size=8, font_weight='bold',with_labels = True)
    plt.tight_layout()
    plt.savefig(os.getcwd()+'/base/static/user/'+login_secretkey+'.png', format="PNG")
    plt.close()
    return True

