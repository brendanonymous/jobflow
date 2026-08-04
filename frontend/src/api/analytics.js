const BASE_URL = "http://localhost:8000"; // TODO: update to env var before deployment

export const fetchSankeyData = async () => {
  const response = await fetch(`${BASE_URL}/analytics/sankey`);

  if (!response.ok) {
    throw new Error(`Failed to fetch Sankey data. Status: ${response.status}`);
  }

  return response.json();
};