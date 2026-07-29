const BASE_URL = "http://localhost:8000"; // TODO: update to env var before deployment

export const fetchApplications = async () => {
  const response = await fetch(`${BASE_URL}/applications`);

  if (!response.ok) {
    throw new Error(`Failed to fetch applications. Status: ${response.status}`);
  }
  
  return response.json();
};