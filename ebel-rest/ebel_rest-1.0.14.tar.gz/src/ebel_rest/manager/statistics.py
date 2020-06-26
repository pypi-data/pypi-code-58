from collections import Counter

import pandas as pd

from ebel_rest.manager.core import Statistics


def summarize() -> Statistics:
    """Returns summary statistics on the graph."""
    return Statistics().apply_api_function('bel_statistics_summarize')


def publication_by_year() -> Statistics:
    """Returns statistics on the number of publications per year in the knowledge graph."""
    return Statistics().apply_api_function('_bel_statistics_publication_by_year')


def publication_by_number_of_statements() -> Statistics:
    """Returns statistics on the number of statements per publication in the knowledge graph."""
    return Statistics().apply_api_function('_bel_statistics_publication_by_number_of_statements')


def last_author_by_number_of_publications() -> Statistics:
    """Returns statistics on the number of publications per author in the knowledge graph."""
    return Statistics().apply_api_function('_bel_statistics_last_author_by_number_of_publications')


def last_author_by_number_of_statements() -> Statistics():
    """Returns statistics on the number of statements per author in the knowledge graph."""
    return Statistics().apply_api_function('_bel_statistics_last_author_by_number_of_statements')


def namespace_by_count() -> Statistics:
    """Returns the number of nodes for each namespace in KG."""
    return Statistics().apply_api_function('bel_statistics_namespace_count')


def node_namespace_order_by_count() -> Statistics():
    """Returns statistics on the frequency of each node type and each namespace in the knowledge graph
    in order of count."""
    return Statistics().apply_api_function('_bel_statistics_node_namespace_order_by_count')


def node_namespace_order_by_namespace() -> Statistics():
    return Statistics().apply_api_function('_bel_statistics_node_namespace_order_by_namespace')


def edges() -> Statistics():
    """Returns statistics on the frequency of each edge type in the knowledge graph."""
    return Statistics().apply_api_function('_bel_statistics_edges')


def nodes() -> Statistics():
    """Returns statistics on the frequency of each node type in the knowledge graph."""
    return Statistics().apply_api_function('_bel_statistics_nodes')


def total_bel_nodes() -> Statistics():
    """Returns the total number of nodes generated from curated statements in the knowledge graph."""
    return Statistics().apply_api_function('bel_statistics_total_bel_nodes')


def total_bel_edges() -> Statistics():
    """Returns the total number of BEL curated edges in the knowledge graph."""
    return Statistics().apply_api_function('bel_statistics_total_stmts')


def total_publications() -> Statistics():
    """Returns the total number of publications in the knowledge graph."""
    return Statistics().apply_api_function('bel_statistics_total_publications')


def subgraphs() -> Statistics():
    return Statistics().apply_api_function('_bel_statistics_subgraph')


def edges_by_pmid(pivot: bool = False):
    """Returns statistics on the frequency of each edge type for each PMID in the knowledge graph.

    Parameters
    ----------
    pivot: bool
        Pivots the generated pandas DataFrame to split the 3 columns (PMID, edge_type, and edge counts) into a new
        DataFrame in which the rows are unique PMIDs and the columns are the different edge types present in the
        knowledge graph.

        If True, this method will return the new DataFrame instead of a Statistics object.

    Returns
    -------
    Statistics or pandas.DataFrame
    """
    stats = Statistics().apply_api_function('bel_statistics_edges_by_pmid')
    if pivot:
        return stats.table.pivot('pmid', 'edge_type', 'count').fillna(0).astype('int')

    else:
        return stats


def nodes_by_pmid(pivot: bool = False):
    """Returns statistics on the frequency of each node type for each PMID in the knowledge graph.

    Parameters
    ----------
    pivot: bool
        Pivots the generated pandas DataFrame to split the 3 columns (PMID, Node Type, and node counts) into a new
        DataFrame in which the rows are unique PMIDs and the columns are the different edge types present in the
        knowledge graph.

        If True, this method will return the new DataFrame instead of a Statistics object.

    Returns
    -------
    Statistics or pandas.DataFrame
    """
    stats = Statistics().apply_api_function('bel_statistics_nodes_by_pmid')
    if pivot:
        data = {'pmid': [], 'Node Type': [], 'counts': []}
        for row in stats.table.itertuples():
            counts = Counter(row.nodes)
            data['pmid'] += (len(counts) * [row.pmid])
            data['Node Type'] += (counts.keys())
            data['counts'] += (counts.values())

        return pd.DataFrame(data).pivot('pmid', 'Node Type', 'counts').fillna(0).astype('int')

    else:
        return stats
