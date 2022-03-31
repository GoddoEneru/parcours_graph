import pandas as pd

problem_df = pd.read_csv("probleme_graphe.csv")

dict_of_correspondence_upstream_downstream = {
    row["noeud_amont"]: row["noeud_aval"] for _, row in problem_df.iterrows()
}

starting_vertices = [row["noeud_amont"] for _, row in problem_df.iterrows() if row["type_aretes"] == "depart"]
ending_vertices = [row["noeud_aval"] for _, row in problem_df.iterrows() if row["type_aretes"] == "arrivee"]


def find_track(data, upstream_vertex):
    path = []
    if upstream_vertex not in ending_vertices:
        downstream_vertex = dict_of_correspondence_upstream_downstream[upstream_vertex]
        path = find_track(data, downstream_vertex)
        path.insert(0, downstream_vertex)
    if upstream_vertex in starting_vertices:
        path.insert(0, upstream_vertex)
    return path


for starting_vertex in starting_vertices:
    print(find_track(problem_df, starting_vertex))
