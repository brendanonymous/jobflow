from collections import Counter
from visualizations.application_snapshot import ApplicationSnapshot
from visualizations.sankey_dto import SankeyDto
from visualizations.utils import get_job_applications # TODO: Rm after POC

def get_link_color(source: str, target: str) -> str:
    """translates an application path into a color"""
    if target == "Rejected":
        return "rgba(255,80,80,0.35)"
    if target == "Offer":
        return "rgba(80,200,120,0.35)"
    if target == "Withdrawn":
        return "rgba(128, 128, 128, 0.35)"
    if target.startswith("Interview"):
        return "rgba(80,140,255,0.35)"
    return "rgba(160,160,160,0.25)"


def generate_sankey_dto() -> SankeyDto:
    applications = get_job_applications("src/visualizations/applications.csv") # TODO: Remove after POC
    edge_counts = Counter()
    for application in applications:
        path = application.status_path

        if len(path) < 2:
            continue

        for src, dst in zip(path, path[1:]):
            edge_counts[(src, dst)] += 1

    node_value_lookup = {
                        "Applied":      0,
                        "Interview 1":  1,
                        "Interview 2":  2,
                        "Interview 3":  3,
                        "Interview 4":  4,
                        "Interview 5":  5,
                        "Interview 6":  6,
                        "Rejected":     7,
                        "Ghosted":      8,
                        "Withdrawn":    9,
                        "Offer":        10
    }

    sources = []
    targets = []
    values = []
    colors = []

    for (src, dst), val in edge_counts.items():
        sources.append(node_value_lookup[src])
        targets.append(node_value_lookup[dst])
        values.append(val)
        colors.append(get_link_color(src, dst))

    
    sankey_dto = SankeyDto(
        sources=sources,
        targets=targets,
        values=values,
        colors=colors
    )

    return sankey_dto